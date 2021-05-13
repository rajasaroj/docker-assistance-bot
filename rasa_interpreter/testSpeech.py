# from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
# from word2number import w2n
# # #load model and tokenizer
# # tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
# # model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# # print("hello")

# a = w2n.word_to_num("first")
import docker
from docker.models.images import Image
import webbrowser
import urllib.request
import difflib




def test1():
    client = docker.from_env()

    a = [x.name for x in client.containers.list()]
    print(a)
    ct = client.containers.list()[3]
    print(ct.name)
    for x in ct.ports:
        # print(x.split("/")[0])
        value = ct.ports[x]
        if value != None:
            print(x)
            print(ct.ports)


            hostIp = value[0]['HostIp']
            hostPort = value[0]['HostPort']
            print(hostIp+ ":" + hostPort)

            url = "http://" + hostIp + ":" + hostPort

            try:
                status = urllib.request.urlopen(url).getcode()
                print(status)
                chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

                if status == 200:
                    webbrowser.get(chrome_path).open(url)
                    break
                else:
                    continue
            except:
                print("URL failed: "+ url)



def test2():

    client = docker.from_env()
    a = [x.name for x in client.containers.list()]
    print(a)

    mystr = "cluster"
    best_match = difflib.get_close_matches(mystr, a, 1)

    result = {}
    print(best_match)
    for word in a:
        canditate = word
        score = difflib.SequenceMatcher(None, mystr, word).ratio()
        print( "score for: " + mystr + " vs. " + word + " = " + str(score))
        result[score] = canditate


    container_name = sorted((float(x),y) for x,y in result.items())[-1][1]
    print(container_name)
    return container_name
    



def fuzzy_string_match(name: str, words_list: list):

    print(words_list)

    mystr = name
    best_match = difflib.get_close_matches(mystr, words_list, 1)

    result = {}
    print(best_match)
    for word in words_list:
        canditate = word
        score = difflib.SequenceMatcher(None, mystr, word).ratio()
        print( "score for: " + mystr + " vs. " + word + " = " + str(score))
        result[score] = canditate


    refined_name = sorted((float(x),y) for x,y in result.items())[-1][1]
    print(refined_name + " = " + refined_name)
    return refined_name



def get_containerid_with_name(word):

    client = docker.from_env()

    container_dict = {}

    for container in client.containers.list():
        container_dict[container.name] = container.id

    container_name_list = list(container_dict.keys())
    container_name = fuzzy_string_match(word, container_name_list)
    container_id = container_dict[container_name]
    print(container_name + " : " + container_id)

    return container_id



get_containerid_with_name("serene")