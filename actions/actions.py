# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

#dispatcher.utter_message(template="utter_ask_launch_cli_or_webpage_form_container_index" ,container_status="Index container data")
#dispatcher.utter_template("utter_ask_launch_cli_or_webpage_form_container_index", tracker=tracker, container_status="Index container data")

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from custom_actions.docker_action_handler import DockerActionHandler
from rasa_sdk.events import SlotSet

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.types import DomainDict

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ActionDockerImagesListProvider(Action):

    def name(self) -> Text:
        return "docker_images_list"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities = tracker.latest_message["entities"]
        print(entities)
        app_feature = []
        
        for e in entities:
            if e["entity"] == "containerization_app_feature":
                app_feature.append(e['value'])
                
        print(app_feature)
        results = DockerActionHandler().list_command_handler(app_feature)
        print(results)
        response = ""

        if "images" in results:
            response = "\n".join([str(image) for image in results["images"] ])
        
        if "containers" in results:
            
            if len(response) > 0 :
                response = response + "\n"

            response += "\n".join([str(container) for container in results["containers"] ])

        dispatcher.utter_message(text=f"{response}")

        return []


class ActionShowContainerStatus(Action):
    
    def name(self) -> Text:
        return "action_ask_launch_cli_or_webpage_form_container_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = DockerActionHandler().show_docker_container_status()
        print(response)

        response = "Please Choose the Container name\n" + response

        dispatcher.utter_message(text=f"{response}")

        return []


class ActionResetSlots(Action):

    def name(self) -> Text:
        return "action_reset_slots"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet(slot, None) for slot in tracker.slots]


class ActionFormSubmit(Action):

    def name(self) -> Text:
        return "action_form_submit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print(tracker.slots)
        DockerActionHandler().start_cli_or_web_container(tracker.get_slot("containerization_app_prompt"), tracker.get_slot("container_name"))

        return []
                


class ValidateLaunchCliAndWebPageForm(FormValidationAction):
    
    def name(self) -> Text:
        return "validate_launch_cli_or_webpage_form"
    
    def validate_containerization_app_command(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict):
        
        print(type(slot_value))
        print(slot_value.isalpha())
        slot_value = slot_value.strip()
        print(slot_value.isalpha())

        if slot_value.isalpha():
            print("-"+slot_value)
            return {"containerization_app_command": slot_value}
        else:
            print(slot_value)
            return {"containerization_app_command": None}

    def validate_containerization_app_prompt(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict):
        print(slot_value)

        if type(slot_value) == list:
            slot_value = slot_value[0].strip()
        else:
            slot_value = slot_value.strip()

        print(slot_value)
        if slot_value.isalpha():
            print("-" + slot_value)
            return {"containerization_app_prompt": slot_value}
        else:
            print(slot_value)
            return {"containerization_app_prompt": None}

    def validate_container_name(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict):
        print("before strip" + slot_value)
        slot_value = slot_value.strip()
        print("after strip" + slot_value)

        if slot_value != "":
            print("-" + slot_value)
            return {"container_name": slot_value}
        else:
            print(slot_value)
            return {"container_name": None}
        