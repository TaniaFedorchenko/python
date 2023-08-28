from collections import UserDict

ADDRESSBOOK = { }

class Addressbook(UserDict):
    
    def add_record(self, data):
        self.data = data
        self.data.append(Record)
        
    
class Field():    # батьківський для всіх полів 
    def __init__(self, name: str, phone: int, record):
        self.name = name 
        self.phone = phone
        self.record = record
    
    
class Record():
    def __init__(self, name: str, phonelist: list,):
        self.name = name 
        self.phonelist = [Phone(phone) for phone in phonelist]

    def add_phone(self, name, phone):
        self.name = name 
        self.phone = phone
        if phone not in self.phonelist:
            self.phonelist.append(phone)
            
        return f"Contact saved as {self.name} with number {self.phone}"
        
        
    def remove_phone(self, data, phone):
        self.data = data
        data[1] = phone
        Record.remove(phone)
        return f"Number {phone} remoded from contsct {self.name}"
        
        
    def change_phone(self, data, phone, name):
        self.phone = phone
        phone = data[1]
        return f"Contact {name} with new phone {phone} was saved"
        
        
    def save_name(self, name):
        self.name = name 
        Record.append(name)
            

class Name(Field):
    
    def __init__(self, name):
        self.name = name 
    
    def name_of_contact(self, name):
        self.name = name 
        return f"Name of contact is {self.name}."
    
    
class Phone(Field):
    def __init__(self, phone):
        self.phone = phone 
        
        
        ## Записи Record у AddressBook зберігаються як значення у словнику. В якості ключів використовується значення Record.name.value. 
        # - пункт 2 в завданні - чомусь я зовсім його не зрозуміла - це повинен бути 1 ключ з такою назвою  чи 3 ключі ?? бо якщо інші частини більщ менш зрозумілі
        # і я намагалась їх втілити , хоч і розумію, що з помилками , то тут я запуталась ()
        
        

    
    