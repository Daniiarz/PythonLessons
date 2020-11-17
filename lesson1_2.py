login = input("Введите ваш логин: ")
password = input("Введите ваш пароль: ")

if login.lower() == "daniiar" and len(password) < 9 and "$"in password:
    print("Вы вошли в систему!!!")
    name = input()
    age = input()
    email = input()
    print(name.title(), age, email)
else:
    if login.lower() != "daniiar":
        print("Не правильный логин")
    if not len(password) < 9 or not "$"in password:
        print("Пароль не подходит")
