import datetime
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value
    
    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return str(self)

class Name(Field):
    pass

class Phone(Field):
    pass

class Birthday(Field):
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
       self.__value = datetime.datetime.strptime(value, "%Y-%m-%d")
    
    def __str__(self):
        return datetime.datetime.strftime(self.__value, "%Y-%m-%d")
            

class Record:
    def __init__(self, name: Name, phone:Phone=None, birthday:Birthday=None):
        self.name = name
        self.phones = [phone] if phone else []
        self.birthday = birthday
        print(self.birthday)
        self.today = datetime.date.today()
        self.birthday_list=str(self.birthday).split('-')
        self.birth = datetime.date(int(self.birthday_list[0]), int(self.birthday_list[1]), int(self.birthday_list[2]))
    def days_to_birthday(self):
        if self.birthday:
            today = datetime.date.today()
            birthday_list=str(self.birthday).split('-')
            birth = datetime.date(int(self.birthday_list[0]), int(self.birthday_list[1]), int(self.birthday_list[2]))
            print("Birth: ", self.birth)
            print("Today:", self.today)
            if (
                today.month == birth.month
                and today.day >= birth.day
                or today.month > birth.month
                ):
                    nextBirthdayYear = today.year + 1
            else:
                nextBirthdayYear = today.year
                nextBirthday = datetime.date(nextBirthdayYear, birth.month, birth.day)
                print("Next birthday: ",nextBirthday)
                diff = nextBirthday - today
                print("Days left for next birthday: ", diff.days)
        else:
            return None
    def __str__(self):
        return f"{self.name} : phones {','.join([str(p) for p in self.phones])} {', birthday: ' + str(self.birthday) if self.birthday else ''}"

class AddressBook(UserDict, Field):
    def add_record(self, rec: Record):
        self.data[rec.name.value] = rec
    
    def iterator():
        def __next__(self):
            if self.current_value < self.MAX_VALUE:
                self.current_value += 1
                return self.current_value
            raise StopIteration

class CustomIterator:
    def __iter__(self):
        return AddressBook()

if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1123123123')
    birthday = Birthday('1995-03-20')
    rec = Record(name, phone, birthday)
    ab=AddressBook()
    ab.add_record(rec)
    print(str(rec))
    print(str(birthday))
    rec.days_to_birthday()
