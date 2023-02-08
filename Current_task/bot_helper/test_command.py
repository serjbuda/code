def error_input(func):
    def inner(command_input):
        print(command_input)
        result = func(command_input)
        return result
    return inner

@error_input
def parser(command_input):
    exit_list = ["close", "exit", "good bye"]
    lower_command=command_input.lower()
    if lower_command in exit_list:
        return 0
    if lower_command == "hello":
        return 1
    if lower_command.startswith("add "):
        return lower_command.replace("add ", "")
    if lower_command == "show all":
        return 2
    if lower_command.startswith("change "):
        lower_command.split()
        return lower_command.split()
    if lower_command.startswith("phone "):
        lower_command.split()
        return lower_command.split()
while True:
    command_input = input("Your input: ")
    parser(command_input)
    print(parser(command_input))
