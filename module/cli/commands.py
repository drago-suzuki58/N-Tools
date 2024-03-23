import module.cli.func

HELP_MESSAGE = """
chapter length : Show the total length of each chapter in each subject

help : Show this message

exit : Exit the program
"""

def commands(s):
    while True:
        user_input = input("Enter Command>>")

        if user_input == "help":
            print(HELP_MESSAGE)

        elif user_input == "chapter length":
            print(module.cli.func.show_chapter_length_list(s))

        elif user_input == "exit":
            break

        else:
            print("\033[31m","Unknown command. Type 'help' for a list of commands.","\033[0m")