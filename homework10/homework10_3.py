from collections import UserDict

ADDRESSBOOK = {}

class Field: 
    def __init__(self, value):  
        self.value = value  
        
class Name(Field):
    pass

class Phone(Field):
    pass
        
        
class Record: 
    def __init__(self, name: Name, phone: Phone = None): 
        self.name = name
        self.phonelist = [] 
        if phone:
            self.phonelist.append(phone)  

    def add_phone(self, phone):
        phone = Phone(phone) 
        if phone not in self.phonelist:
            self.phonelist.append(phone)

        return f"Contact saved as {self.name.value} with number {phone.value}"

    def remove_phone(self, phone):
        phone = Phone(phone)
        for ph_object in self.phonelist:
            if ph_object.value == phone.value: 
                self.phonelist.remove(ph_object)
        return f"Number {phone.value} remoded from contsct {self.name.value}"

    def change_phone(self, old_phone, new_phone):
        for ph_object in self.phonelist:
            if ph_object.value == old_phone:
                ph_object.value = new_phone # якщо телефон співпадає замінюємо новим
        return f"Contact {self.name.value} with new phone {new_phone} was saved"
    
class AddressBook(UserDict):

    def add_record(self, record: Record): 
        self.data[record.name.value] = record
        

if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    print(ab)
    
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phonelist, list)
    assert isinstance(ab['Bill'].phonelist[0], Phone)
    assert ab['Bill'].phonelist[0].value == '1234567890'

    print('All Ok)')

    