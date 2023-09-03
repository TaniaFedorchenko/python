from collections import UserDict
from datetime import datetime, timedelta
from random import randint
import json

ADDRESSBOOK = {}


class Field:
    def __init__(self, value):
        self.__value = None  
        self.value = value


class Name(Field):
    pass
   

class Phone(Field):

    def __init__(self, phone):  
        self.__phone = None 
        self.phone = phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if len(phone) < 10:
            print("You entered an incorrect number. Please, change number")
        else:
            self.__phone = phone  
            print("Your number appended to contacts!")
            
            
class Birthday(Field):
    def __init__(self, birthday):
        self.__birthday = None
        self.birthday = birthday

    @property
    def birthday(self):  
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        try:
            self.__birthday = datetime.strptime(value, "%Y-%m-%d").date()  
        except Exception:
            print(f"Format not correct, example: YYYY-MM-DD")
            
class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None, ):
        
        self.name = name
        self.birthday = birthday if birthday else None  # якщо передадуть обьект дня народження то запишемо
        self.phonelist = []
        if phone:
            self.phonelist.append(phone)

    def add_phone(self, phone):
        phone = Phone(phone)
        if phone not in self.phonelist:
            self.phonelist.append(phone)

        return f"Contact saved as {self.name.value} with number {phone.phone}"

    def remove_phone(self, phone):
        phone = Phone(phone)
        for ph_object in self.phonelist:
            if ph_object.value == phone.value:
                self.phonelist.remove(ph_object)
        return f"Number {phone.phone} remoded from contsct {self.name.value}"

    def change_phone(self, old_phone, new_phone):
        for ph_object in self.phonelist:
            if ph_object.value == old_phone:
                ph_object.value = new_phone  # якщо телефон співпадає замінюємо новим
        return f"Contact {self.name.value} with new phone {new_phone} was saved"

    def days_to_birthday(self):
        
        if self.birthday:  
            current_day = datetime.now().date()
            this_year_bd = self.birthday.birthday.replace(year=current_day.year) 
            days_before_birthday = this_year_bd - current_day
            if days_before_birthday.days < 0:  
                next_year_bd = self.birthday.birthday.replace(year=current_day.year + 1)
                days_before_birthday = next_year_bd - current_day

            return f"Days before the birthday: {days_before_birthday.days}"
        else:  
            return f"Birthday for user {self.name.value} not found"

    def __str__(self):
        return f"{self.name.value} {[ph.phone for ph in self.phonelist]} {self.birthday.birthday if self.birthday else ''}"

    
    
class AddressBook(UserDict):
    N = 2 
    
    def dump(self):
        with open(self.file, "w") as f:
            json.dump(self.record_id, self.records, f)
    
    def load(self):
        if not self.f.exists():
            return
        with open(self.file, "r") as f:
            self.record_id, self.records = json.load(f)
    

    def searcher(self, search: str):
        result = []
        for record_id, record in self.records.items():
            if search in record:
                result.append(record_id)
            return result
    

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def iterator(self, n=None):
        if n:
            AddressBook.N = n
        return self.__next__()
    
    def __iter__(self):
        n_list = []
        counter = 0
        contact_list = list(self.data.values()) 

        for contact in contact_list:
            n_list.append(contact)
            counter += 1
            if counter >= AddressBook.N: 
                yield n_list
                n_list.clear()
                counter = 0
        yield n_list

    def __next__(self):
        generator = self.__iter__()
        page = 1
        while True:
            user_input = input("Press ENTER")
            if user_input == "":
                try:
                    result = next(generator)
                    if result:
                        print(f"{'*' * 20} Page {page} {'*' * 20}")
                        page += 1
                    for var in result:
                        print(var)
                except StopIteration:
                    print(f"{'*' * 20} END {'*' * 20}")
                    break
            else:
                break



if __name__ == "__main__":
    ab = AddressBook()

    name = Name('Bill')
    phone = Phone('+380978009090')
    birthday = Birthday("2000-9-10")
    rec = Record(name, phone, birthday)
    ab.add_record(rec)
    print(ab)

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phonelist, list)
    assert isinstance(ab['Bill'].phonelist[0], Phone)
    assert isinstance(ab['Bill'].days_to_birthday(), str)
    assert ab['Bill'].phonelist[0].phone == '+380978009090'

    print('All Ok)')

    
    print(rec.days_to_birthday()) 
    
    

    # Додамо юзерів щоб протестити ітератор
    name1 = Name('Іван')
    phone1 = Phone('+380978009091')
    birthday1 = Birthday("2000-1-10")
    rec1 = Record(name1, phone1, birthday1)
    ab.add_record(rec1)

    name2 = Name('Олег')
    phone2 = Phone('+380978009092')
    birthday2 = Birthday("2000-12-10")
    rec2 = Record(name2, phone2, birthday2)
    ab.add_record(rec2)

    name3 = Name('Тетьяна')
    phone3 = Phone('+380978009093')
    birthday3 = Birthday("2000-11-10")
    rec3 = Record(name3, phone3, birthday3)
    ab.add_record(rec3)

    name4 = Name('Влад')
    phone4 = Phone('+380978009094')
    birthday4 = Birthday("2000-9-10")
    rec4 = Record(name4, phone4, birthday4)
    ab.add_record(rec4)
    
    name5 = Name('Артем ')
    phone5 = Phone('+380965743297')
    birthday5 = Birthday("2000-3-5")
    rec5 = Record(name5, phone5, birthday5)
    ab.add_record(rec5)
    
    name6 = Name('Олександр')
    phone6 = Phone('+380939834275')
    birthday6 = Birthday("2000-15-9")
    rec6 = Record(name6, phone6, birthday6)
    ab.add_record(rec6)
    
    name7 = Name('Оксана')
    phone7 = Phone('+380959098809')
    birthday7 = Birthday("2000-4-8")
    rec7 = Record(name7, phone7, birthday7)
    ab.add_record(rec7)
    
    name8 = Name("Вікторія")
    phone8 = Phone('+380504919825')
    birthday8 = Birthday("2000-5-12")
    rec8 = Record(name8, phone8, birthday8)
    ab.add_record(rec8)
    
    name9 = Name('Андрій')
    phone9 = Phone('+380634569098')
    birthday9 = Birthday("2000-9-10")
    rec9 = Record(name9, phone9, birthday9)
    ab.add_record(rec9)
    
    name10 = Name('Людмила')
    phone10 = Phone('+380998071264')
    birthday10 = Birthday("2000-5-8")
    rec10 = Record(name10, phone10, birthday10)
    ab.add_record(rec10)
 

    ab.iterator(n=3)  


         