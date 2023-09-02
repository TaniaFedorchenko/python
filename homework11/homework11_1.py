from collections import UserDict
from datetime import datetime
from random import randint

ADDRESSBOOK = {}

class Field: 
    def __init__(self, value):  
        self.value = value  
        

        
class Name(Field):
    pass
    ###
    # def __init__(self, name): 
        # self.__name = name
        
    # @property
    # def name(self):
        # return self.__name
    
    # @name.setter
    # def name(self, value):
        # if value == None:
            # print("Please, enter your name!")
        # lse:
            # print("Your name appended to contacts!")
    
            
            

class Phone(Field):
    
    def __init__(self, phone):  # changed value on phone
        self.__phone = phone
        
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, phone):
        if len (phone)!= 10 or len (phone)!= 12:
            print("You entered an incorrect number. Please, change number")
        else:
            print("Your number appended to contacts!")  

                                                            # Перевірку на коректність веденого номера телефону setter для value класу Phone.
                                                                
class Birthday(Field):
    def __init__(self, birthday): 
        self.__birthday = birthday
        
    @property
    def days_to_birthday(self):
        return self.__birthday
    
    @days_to_birthday.setter
    def days_to_birthday(self, value):
        if len (value)!= 10 or len (value)!= 12:
            print("You entered an incorrect number. Please, change number")
        else:
            print("Your number appended to contacts!") 
    

                                                                         # Перевірку на коректність веденого дня народження setter для value класу Birthday.
    
        
class Record: 
    def __init__(self, name: Name, phone: Phone = None, birthday = Birthday): 
        self.name = name
        self.birthday = birthday
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
    
    def days_to_birthday(self, birthday):  
        birthday = Birthday(birthday)                                
        self.current_day = current_day
        current_day = datetime.now()
        birthday = datetime.strftime('%Y, %B, %D')
        days_before_birthday = self.birthday - self.current_day
        
        return f"Days before the birthday: {days_before_birthday}"
        
        
        # Додамо функціонал роботи з Birthday у клас Record, а саме функцію days_to_birthday, яка повертає кількість днів до наступного дня народження.
        # Клас Record реалізує метод days_to_birthday, який повертає кількість днів до наступного дня народження контакту, якщо день народження заданий.
        
    
class AddressBook(UserDict):

    def add_record(self, record: Record): 
        self.data[record.name.value] = record
        
    def iterator(self, record: Record, quantity, max_quantity):
        self.quantity = quantity
        quantity = 0
        max_quantity = 10
        
        for record in ADDRESSBOOK:
            contact_list = []
            if quantity <1:
                return f"Please, enter an additional number to get a list"
            elif quantity > max_quantity:
                print(f"List can't contain more than {max_quantity} entries per page")
                return contact_list
            else:
                contact_list.uppend(record)
                quantity +=1
                return contact_list
            
            # скоріше за все саме цей пунтк неправильний зовсімб але багато читала прикладів  про генератори і там скрізь  створюється клас ,
            # а в умові як я зрозуміла , треба щоб це був метод в класіAddressBook. 
            
            # а ще як я розумію потрібно , щоб кожна наступна ітерація показувала нам наступну сторінку списку , але  я не знаю, як це зробити .
            # тому прошу допомоги 
        
            
        
    # Додамо пагінацію (посторінковий висновок) для AddressBook для ситуацій, коли книга дуже велика і треба показати вміст частинами,
    # а не все одразу. Реалізуємо це через створення ітератора за записами.
    
    # AddressBook реалізує метод iterator, який повертає генератор за записами AddressBook і за одну ітерацію повертає уявлення для N записів.
        

if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    birthday = Birthday("2000-9-10")
    rec = Record(name, phone, birthday)
    ab = AddressBook()
    ab.add_record(rec)
    print(ab)
    
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phonelist, list)
    assert isinstance(ab['Bill'].phonelist[0], Phone)
    # assert isinstance(ab['Bill'].days_to_birthday, Birthday)
    assert ab['Bill'].phonelist[0].value == '1234567890'

    print('All Ok)')

    