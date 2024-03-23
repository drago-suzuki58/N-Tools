import module.cli.init
import module.cli.commands as commands

def main():
    try:
        s = module.cli.init.login()
        commands.commands(s)
    except Exception as e:
        print(f"An error occurred: {e}") #!debug

if __name__ == '__main__':
    main()