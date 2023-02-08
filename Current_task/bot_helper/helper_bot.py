def error_input(func):
    def inner(command_input):
        check_list=["close", "exit", "good bye","hello","good bye","show all"]
        com=command_input.lower()
        command_split = com.split()
        if command_input.lower() in check_list and len(command_split) in range(3):
            result = func(command_input)
            return result
        elif command_split[0] == 'add' and len(command_split) < 3:
            print("Give me name and phone please.")
        elif command_split[0] == 'phone' and len(command_split) < 2:
            print("Enter user name.")
        elif command_split[0] == 'change' and len(command_split) < 3:
            print("Give me name and phone please.")
        elif command_split[0] == 'add' and len(command_split) == 3:
            result = func(command_input)
            return result
        elif command_split[0] == 'phone' and len(command_split) == 2:
            result = func(command_input)
            return result
        elif command_split[0] == 'change' and len(command_split) == 3:
            result = func(command_input)
            return result
        else:
            print("Input correct command.")
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
    
def handler(parser_output):
    name_phone_dict = {}
    if type(parser_output) == str:
        split_list=parser_output.split()
        name_phone_dict.update({"Name": split_list[0].capitalize(), "Phone": split_list[1]})
        return name_phone_dict
    elif type(parser_output) == list:
        return parser_output
    
def main():
    all_contacts_list=[]
    while True:
        print("Command list: hello, add ..., change ..., phone ..., show all, good bye, close, exit.")
        command_input = input("Input command: ")
        parser(command_input)
        parser_output=parser(command_input)
        if parser_output == 0:
            print("Good bye!")
            exit() 
        elif parser_output == 1:
            print("How can I help you?")
        elif parser_output == 2:
            print("List of all contacts: ", all_contacts_list)
        else:
            handler(parser_output)
            handler_output=(handler(parser_output))
            if type(handler_output)==dict:
                all_contacts_list.append(handler_output)
            elif type(handler_output)==list:
                if handler_output[0] == "phone":
                    for i in all_contacts_list:
                        nm=i.get("Name")
                        ph=i.get("Phone")
                        if handler_output[1] == nm.lower():
                            print(f"{nm}'s phone is:",ph)
                        else:
                            print(f"Name {handler_output[1].capitalize()} is not found in contacts.")
                elif handler_output[0] == "change":
                    for i in all_contacts_list:
                        nm=i.get("Name")
                        if handler_output[1] == nm.lower():
                            i["Phone"] = handler_output[2]
                            print(f"{handler_output[1].capitalize()}'s phone changed to {handler_output[2]}")
                        else:
                            print(f"Name {handler_output[1].capitalize()} is not found in contacts.")
if __name__ == "__main__":
    main()
