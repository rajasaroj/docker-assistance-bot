
from custom_actions.terminal_command_handler import CommandLineInterfaceHandler
#from terminal_command_handler import CommandLineInterfaceHandler


class DockerAwsAuthenticationHandler:


    def aws_login(region: str, username: str, ecr_uri: str):

        command = f"aws ecr get-login-password --region {region} | docker login --username {username} --password-stdin {ecr_uri}"
        print(command)
        CommandLineInterfaceHandler.launch_terminal_with_command(command)

