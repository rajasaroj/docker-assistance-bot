import subprocess
import os
import time

class CommandLineInterfaceHandler:

    def launch_terminal_with_command(command: str):
        fname = ""
        with open("start_node.command", "w") as f:
            cmd = command
            f.write(f"#!/bin/sh\n {cmd} \n")
            subprocess.call(['chmod', '775', f.name])
            fname = f.name

        subprocess.call(['open', '-n', '-a', 'Terminal', fname])
        time.sleep(2)
        os.remove(fname)


    def run_command_same_terminal(command):
        container_status = subprocess.run(command, capture_output=True, text=True).stdout
        print(container_status)
        return container_status


# how to use eg:
# "docker exec -it cbcbf943a0fb /bin/sh"
#CommandLineInterfaceHandler.run_command_same_terminal("docker exec -it cbcbf943a0fb /bin/sh")