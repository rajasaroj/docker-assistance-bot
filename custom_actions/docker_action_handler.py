
from custom_actions.docker_garage import DockerHelper
import difflib
from custom_actions.docker_aws_authenticate_handler import DockerAwsAuthenticationHandler


class DockerActionHandler:

    def __init__(self):
        self.dockerHelper = DockerHelper()


    def __fuzzy_string_match(self, name: str, words_list: list):
        
        if type(name) == list:
            name = " ".join(name)

        print(words_list)
        mystr = name
        best_match = difflib.get_close_matches(mystr, words_list, 1)

        result = {}
        print(best_match)
        for word in words_list:
            canditate = word
            score = difflib.SequenceMatcher(None, mystr, word).ratio()
            print( "score for: " + str(mystr) + " vs. " + str(word) + " = " + str(score))
            result[score] = canditate


        refined_name = sorted((float(x),y) for x,y in result.items())[-1][1]
        print(refined_name + " = " + refined_name)
        return refined_name



    def __get_containerid_using_name(self, word):

        container_dict = {}

        for container in self.dockerHelper.list_all_containers():
            container_dict[container.name] = container.id

        container_name_list = list(container_dict.keys())
        container_name = self.__fuzzy_string_match(word, container_name_list)
        container_id = container_dict[container_name]
        print(container_name + " : " + container_id)

        return container_id
        

    def list_command_handler(self, entities):

        isImages = False
        isContainers = False

        results = {}

        for x in entities:

            if x == "image" or x == "images":
                print("images")
                results["images"] = self.dockerHelper.list_all_images()
            
            elif x == "container" or x == "containers":
                print("containers")
                results["containers"] = [container.name for container in self.dockerHelper.list_all_containers()]
            
            else:
                print("nothing")
        
        return results


    def show_docker_container_status(self):
        return self.dockerHelper.show_containers_status()


    def __get_id_with_container_idx(self, container_idx):

        containers = self.dockerHelper.list_all_containers()
        try:
            if container_idx <= len(containers):
                return [container.id for container in self.dockerHelper.list_all_containers()][container_idx-1]
        except:
            print("Invalid Container Index")
            return None


    def __get_container_using_id(self, container_id):

        for container in self.dockerHelper.list_all_containers():
            if container.id == container_id:
                return container

 

    def start_cli_or_web_container(self, command, container_name):
        #container_idx = int(container_idx)

        container_id = self.__get_containerid_using_name(container_name)
        print(container_id)

        if command == "cli": 
            self.dockerHelper.launch_container_cli(container_id)
        else:
            # TODO
            print("work in progress --> web page feature")
            self.dockerHelper.launch_container_webpage(self.__get_container_using_id(container_id))


    def authenticate_with_aws(self, region: str, username: str, ecr_uri: str):
        DockerAwsAuthenticationHandler.aws_login(region, username, ecr_uri)







#DockerActionHandler().start_cli_or_web_container('cli', 1)