import webbrowser
import urllib.request



class BrowserCommandHandler:


    def launch_container_webpage_on_browser(container):

        for key in container.ports:
            value = container.ports[key]
            if value != None:
                print(key)
                print(container.ports)
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





# How to run to test: uncomment below and make sure there are conatiners running which exposes dashboards for browser
# import docker
# from docker.models.images import Image
# client = docker.from_env()
# a = [x.name for x in client.containers.list()]
# print(a)
# ct = client.containers.list()[container_index]
# BrowserCommandHandler.launch_container_webpage(ct)
