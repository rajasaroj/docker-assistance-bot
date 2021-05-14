import docker
from docker.models.images import Image
from docker.models.containers import Container
from docker.types import containers
from custom_actions.terminal_command_handler import CommandLineInterfaceHandler
from custom_actions.webbrowser_comand_handler import BrowserCommandHandler


class DockerHelper:

    def __init__(self):
        self.client = docker.from_env()


    def list_all_images(self):
        return self.client.images.list()

    def list_all_containers(self): 
        return self.client.containers.list()

    def launch_container_cli(self, containerId: str):
        cmd = f"docker exec -it {containerId} /bin/sh"
        CommandLineInterfaceHandler.launch_terminal_with_command(command=cmd)

    def launch_container_webpage(self, container: Container):
        print(container.name)
        BrowserCommandHandler.launch_container_webpage_on_browser(container)

    def show_containers_status(self):
        cmd = ['docker', 'ps', '-a']
        return CommandLineInterfaceHandler.run_command_same_terminal(cmd)
    
    def show_images_status(self):
        cmd = ['docker', 'images']
        return CommandLineInterfaceHandler.run_command_same_terminal(cmd)

    
    def pull_docker_images(self, image_url):
        command = f"docker pull {image_url}"
        print(command)
        CommandLineInterfaceHandler.launch_terminal_with_command(command)







# How to use the service for test eg below:
# DockerHelper().launch_container_cli("cbcbf943a0fb")
# DockerHelper().show_images_status()
# DockerHelper().show_containers_status()
#DockerHelper().pull_docker_images("957633371688.dkr.ecr.us-east-1.amazonaws.com/consul:latest")