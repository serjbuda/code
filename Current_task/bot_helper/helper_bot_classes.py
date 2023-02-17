from collections import UserDict
import re
class Bot:
    all_contacts_list = []
    def __init__(self, command_input, lower_command, command_split):
        self.command_input = command_input
        self.lower_command = lower_command
        self.command_split = command_split
    def error_cases(self):
        check_list=["close", "exit", "good bye","hello","good bye","show all"]
        if lower_command in check_list and len(command_split) in range(3):
            return self.command_input
        elif command_split[0] == 'add' and len(command_split) < 3:
            print("Give me name and phone please.")
        elif command_split[0] == 'phone' and len(command_split) < 2:
            print("Enter user name.")
        elif command_split[0] == 'change' and len(command_split) < 3:
            print("Give me name and phone please.")
        elif command_split[0] == 'add' and len(command_split) == 3:
            if len(re.findall(r"[a-zA-Z]", command_split[2])) >0:
                print("Phone number cannot contain characters.")
        elif command_split[0] == 'change' and len(command_split) == 3:
            if len(re.findall(r"[a-zA-Z]", command_split[2])) >0:
                print("Phone number cannot contain characters.")
        elif command_split[0] == 'record':
            print("Record commnad")
        elif command_split[0] == 'phones':
            print("Phones commnad")
        elif command_split[0] == 'names':
            print("Names commnad")
        else:
            print("Input correct command.")
    def command_operator(self):
        name_phone_dict = {}
        exit_list = ["close", "exit", "good bye"]
        if self.lower_command in exit_list:
            print("Good bye!")
            exit()
        if self.lower_command == "hello":
            print("How can I help you?")
        if self.lower_command.startswith("add ") and len(re.findall(r"[a-zA-Z]", command_split[2]))==0:
            name_phone_dict.update({"Name": command_split[1].capitalize(), "Phone": command_split[2]})
            self.all_contacts_list.append(name_phone_dict)
            print(f"Contact with name {command_split[1].capitalize()} and phone {command_split[2]} added")
        if self.lower_command == "show all":
            print("List of all contacts: ", self.all_contacts_list)
        if self.command_split[0] == "phone":
            for i in self.all_contacts_list:
                nm=i.get("Name")
                ph=i.get("Phone")
                if command_split[1] == nm.lower():
                    print(f"{nm}'s phone is:",ph)
                else:
                    print(f"Name {command_split[1].capitalize()} is not found in contacts.")
        elif self.command_split[0] == "change" and len(re.findall(r"[a-zA-Z]", command_split[2]))==0:
            for i in self.all_contacts_list:
                nm=i.get("Name")
                if self.command_split[1] == nm.lower():
                    i["Phone"] = self.command_split[2]
                    print(f"{command_split[1].capitalize()}'s phone changed to {command_split[2]}")
                else:
                    print(f"Name {command_split[1].capitalize()} is not found in contacts.")
class Field:
    pass                
class AddressBook(UserDict, Field):
    def add_record(self, value):
        return value in self.data.values()
class Record(Bot, Field):
    def __init__(self, lower_command):
        self.lower_command = lower_command
    def name_phone_record(self):
        if lower_command == 'record':
            print(self.all_contacts_list)
class Name(Record, Field):
    name = ''
class Phone(Record, Field):
    phone = ''
if __name__ == "__main__":
    while True:
        print("Bot command list: hello, add ..., change ..., phone ..., show all, good bye, close, exit.")
        print("Class comands: record")
        command_input = input("Input your command: ")
        lower_command=command_input.lower()
        command_split=lower_command.split()
        bot = Bot(command_input, lower_command, command_split)
        record = Record(lower_command)
        bot.error_cases()
        bot.command_operator()
        record.name_phone_record()
