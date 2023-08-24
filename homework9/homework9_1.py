import sys

ADDRESSBOOK = {}


def input_error(inner):
    def wrap(*args):
        try:
            return inner(*args)
        except IndexError:
            return "Give me name and phone please"
        except KeyError:
            return "Write correct name please"
        except ValueError:
            return " Write correct number phone  please"
    return wrap


@input_error
def hello_handler(*args):
    return "Hello can I help you?"

@input_error
def add_handler(data):  # Функції обробники команд
    name = data[0].title()
    phone = data[1]
    ADDRESSBOOK[name] = phone
    return f"Contact {name} with phone {phone} was saved"


def change_handler(data): # додаю умову 4.3   \ return немає, бо за умовою функція нічого не поверта. Можливо , тут помилка 
    name = data[0].title()
    phone = data[1]
    phone_new = phone.replace(data[1])
    ADDRESSBOOK[name] = phone_new
    return f"New contact {name} with phone {phone_new} was saved"
    

  
def phone_hangler(name): # додаю умову 4.4
    for key, value in ADDRESSBOOK.items():
        if name in key:
            return value
    
    #if name in ADDRESSBOOK:
        #phone = ADDRESSBOOK.get(name)
        #return phone
    return 'Write correct name please '


def show_all_handler():
    return ADDRESSBOOK


def exit_handler(*args):
    return "Good bye!"


@input_error
def command_parser(raw_str: str):  # Парсер команд
    elements = raw_str.split()
    for key, value in COMMANDS.items():
        if elements[0].lower() in value:
            return key(elements[1:])
    return "Unknown command"


COMMANDS = {
    hello_handler: ["hello"], 
    add_handler: ["add", "додай", "+"],
    change_handler: ["change", "замінити номер", "change number"],
    phone_hangler: ["show number", "number", "номер телефону"],
    show_all_handler: ["book", "phones"], 
    exit_handler: ["good bye", "close", "exit", "."]
    }


def main():  # Цикл запит-відповідь.
    while True:
        user_input = input(">>> ")  # add Vlad 0987009090
        result = command_parser(user_input)
        print(result)
        if result == "Good bye!" or ".":   # додала умову 2
            break


if __name__ == "__main__":
    main()