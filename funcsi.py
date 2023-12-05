import json
from users import User, get_data


def register():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    birth_date = input('Enter your birth_date: ')
    email = input('Enter your email: ')
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    with open(r'D:\SHOXRUX\Foundation\BUTCAMP\Python\Exam\2 - modul\users.json', 'r') as file:
        users = json.load(file)
        for user in users:
            if user['username'] == username:
                print("This username is already in use. Please choose another one.")
                return register()


    user = User(first_name, last_name,birth_date, email, username, password)
    user.append_to_json()
    

def login():
    username = input('Enter the username: ')
    password = input('Enter the password: ')
    users = get_data()
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user['id']
    return 0
