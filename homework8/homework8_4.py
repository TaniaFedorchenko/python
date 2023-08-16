from datetime import datetime, timedelta

users = (
    {'name': 'Tania', 'birthday': '17-08-2000'},
    {'name': 'Lilia', 'birthday': '10-08-2000'},
    {'name': 'Denis', 'birthday': '19-08-2000'},
    {'name': 'Volodimir', 'birthday': '07-07-2000'},
    {'name': 'Dmitro', 'birthday': '31-08-2000'},
    {'name': 'Artem', 'birthday': '21-08-2000'})

# краще заведемо словник з кожним днем тиждня і пустим списком куди будемо додаваю юзерів якщо в них в цей день День Народження
birthday_weekdays = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [],
                     "Friday": [], "Saturday": [], "Sunday": [], "next Monday": []}


def get_birthdays_per_week(date: str):

    # знайдемо поточну дату тобто сьогодні
    current_date = datetime.now().date()
    # знайдемо який сьогодні номер дня
    current_weekday = current_date.weekday()
    # згідно умові тиждень починається з понеділка тобто з 0
    start_point = current_date - timedelta(days=current_weekday) # це наша стартова точка
    # і закінчується неділею, тобто 6
    end_point = start_point + timedelta(days=6)  # це кінцева точка

    for user in users: # ітеруємо по кожному юзеру
        username = user.get("name")

        user_birthday = user.get("birthday")
        # d, m, y = date.split('-')  # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
        # date = datetime(day=int(d), month=int(m), year=int(y))  # таке собі рішення, краще через вбудований формат
        date_obj = datetime.strptime(user_birthday, "%d-%m-%Y").date()  # це вже обьект дататайм і тільки дата без часу

        user_birthday_dt = date_obj.replace(year=current_date.year) # замінюємо рік народження на поточний, щоб була можливість порівнювати дати між початком і кінцем тиждня

        if start_point <= user_birthday_dt <= end_point: # тут робимо перевірку через яку пройдуть тільки ті юзери у яких день народження в межах поточного тиждня
            user_weekday = user_birthday_dt.weekday() # тут отримаємо номер дня у якого у юзера день народження
            if user_weekday in [0]: # якщо цей день 0 то додаємо в наш словник по ключу Monday
                birthday_weekdays["Monday"].append(username)
            # далі перевірте кожень день
            if user_weekday in [1]: 
                birthday_weekdays["Tuesday"].append(username)
            if user_weekday in [2]: 
                birthday_weekdays["Wednesday"].append(username)
            if user_weekday in [3]: 
                birthday_weekdays["Thursday"].append(username)
            if user_weekday in [4]: 
                birthday_weekdays["Friday"].append(username)
            if user_weekday in [5]: 
                birthday_weekdays["Monday"].append(username)
            if user_weekday in [6]: 
                birthday_weekdays["Monday"].append(username)
        


    print(f'Monday:{birthday_weekdays["Monday"]}')    
    print(f'Tuesday:{birthday_weekdays["Tuesday"]}')   
    print(f'Wednesday:{birthday_weekdays["Wednesday"]}') 
    print(f'Thursday:{birthday_weekdays["Thursday"]}') 
    print(f'Friday:{birthday_weekdays["Friday"]}')   


                           
    # після цього роздрукуйте гарно за допомгою f-строки отриманні данні словника birthday_weekdays

if __name__ == "__main__":
    get_birthdays_per_week(users)


