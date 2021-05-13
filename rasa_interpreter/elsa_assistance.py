from typing import Text
import speech_recognition as sr
import subprocess
import requests
from rasa_interpreter.mic_input_ai import SpeechRecognition as SpeechRecognitionAI
from word2number import w2n

class Elsa:

    def say(text):
        subprocess.call(['say', text])
    

    def triggerConversation(text: str):
        query = text
        url = 'http://localhost:5005/webhooks/rest/webhook'
        myobj = {"sender":"Me","message":query}
        headers = {'content-type': 'application/json'}
        r = requests.post(url, json=myobj, headers=headers)
        y = r.text
        print(y)


    def startTalking():
        #r = sr.Recognizer()
        #mic = sr.Microphone()
        speech_recognition_ai = SpeechRecognitionAI()

        Elsa.say("Hi Raja Please a say something")
        print("say anything : ")
        # text= speech_recognition_ai.start_speech_recognition(record_seconds=5, debug=True)
        # print(text)
        while True :

            try:
                print("Recognizing...")

                text= speech_recognition_ai.start_speech_recognition(record_seconds=5, debug=True)
                if text.lower() == "goodbye" or text.lower() == "good bye":
                    Elsa.say("Goodbye")
                    break
                print(text)
                #Elsa.triggerConversation(text)
            except:
                print("sorry, could not recognise")


    # def startTalking2():
    #     r = sr.Recognizer()
    #     mic = sr.Microphone()

    #     with mic as audio_file:
    #         print("Speak Please")



    #         #print("Converting Speech to Text...")
    #         Elsa.say("Hi Raja Please a say something")

    #         try:

    #             r.adjust_for_ambient_noise(audio_file)
    #             audio = r.listen(audio_file)
    #             #text = r.recognize_google(audio)
    #             text = r.recognize_ibm(audio)
    #             r.recognize_google_cloud()
    #             print("You said: " + text)

    #             if text.lower() == "goodbye" or text.lower() == "good bye":
    #                 Elsa.say("Goodbye")
                    
    #             Elsa.triggerConversation(text)

    #         except Exception as e:
    #             print("Error: " + str(e))





    
Elsa.startTalking()








        # Elsa.say("Hi Raja Please a say something")
        # print("say anything : ")
        
        # while True :

        #     try:
        #         print("Recognizing...")
        #         text= 
        #         print(text)
        #            text= speech_recognition_ai.start_speech_recognition(record_seconds=5, debug=True)
        #         if text.lower() == "goodbye" or text.lower() == "good bye":
        #             Elsa.say("Goodbye")
        #             break
        #         print(text)
        #         #Elsa.triggerConversation(text)
        #     except:
        #         print("sorry, could not recognise")