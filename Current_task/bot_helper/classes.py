from collections import UserDict
class Field:
    def __init__(self, value):
        self.value = value
class Name(Field):
    pass
class Phone(Field):
    pass
class Record(Field):
    def __init__(self, name: Name, phone:Phone=None):
        self.name = name
        self.phones = [phone] if phone else []
class AddressBook(UserDict, Field):
    def add_record(self, rec: Record):
        self.data[rec.name.value] = rec

if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1123123123')
    rec = Record(name, phone)
    ab=AddressBook()
    ab.add_record(rec)
    
