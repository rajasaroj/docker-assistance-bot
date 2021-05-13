import requests
from elsa_assistance import Elsa


def triggerConversation():



    #query = "show me list of docker images"
    
    query = Elsa.startTalking()
    url = 'http://localhost:5005/webhooks/rest/webhook'
    myobj = {"sender":"Me","message":query}
    headers = {'content-type': 'application/json'}
    
    r = requests.post(url, json=myobj, headers=headers)
    y = r.text
    print(y)

triggerConversation()