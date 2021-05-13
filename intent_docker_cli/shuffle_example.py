import random

def suffle_examples():

    f = open("/Users/rsaroj/code_space/rasa-init-demo/intent_docker_cli/align_open_docker_cli_examples_exp_data.txt", "r")
    example_list = f.readlines()
    random.shuffle(example_list)
    random.shuffle(example_list)
    random.shuffle(example_list)

    with open('somefile2.txt', 'a') as the_file:
        
        for x in example_list:
            the_file.write(x)

suffle_examples()