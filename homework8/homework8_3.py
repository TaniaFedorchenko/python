from datetime import datetime

users = (
    { 'name': 'Tania', 'birthday': '17-08-2000'}, 
    { 'name': 'Lilia', 'birthday': '10-08-2000'},
    { 'name': 'Denis', 'birthday': '19-08-2000'},
    { 'name': 'Volodimir', 'birthday': '07-07-2000'},
    { 'name': 'Dmitro', 'birthday': '31-08-2000'},
    { 'name': 'Artem', 'birthday': '21-08-2000'} )

name_of_day = {
    0: 'monday',
    1: 'tuesday',
    2: 'wednesday',
    3: 'thuesday',
    4: 'friday', 
    5: 'saturday',
    6: 'sunday'}

day_of_birthday = {
    'monday': 0,
    'tuesday': 0,
    'wednesday': 0,
    'thuesday': 0,
    'friday': 0, 
    'saturday': 0,
    'sunday': 0}

def get_birthdays_per_week(date: str):
    d, m, y =  date.split('-')
    date = datetime(day=int(d), month=int(m), year=int(y))
    
    birthday_day = name_of_day.get(date.weekday())  #  визначення дня тижня, що вводить користувач 
    if birthday_day in day_of_birthday:   # якщо день співпадає з днем по ключу  в списку users,  то  додати імя  по ключу name в список day of birthday
        day_of_birthday.get(users['name'])
    return day_of_birthday


                                                              #",". join(["a", "b", "c"]) -> "a,b,c" . Разделитель пишут в кавычках перед join, в список должен состоять из строк.
    

print(get_birthdays_per_week('19-08-2000'))