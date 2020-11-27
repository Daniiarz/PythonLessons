class Account:

    def __init__(self, login, password):
        self._login = login
        self._password = password

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        print("Login can't be changed!!!")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if len(value) < 6:
            print('Incorrect password')
        else:
            self._password = value


class InstagramAccount(Account):

    def __init__(self, login, password, name, surname):
        super(InstagramAccount, self).__init__(login, password)
        self._name = name
        self._surname = surname


class FaceBookAccount(Account):

    def __init__(self, login, password, work_place, date_of_birth, location):
        super(FaceBookAccount, self).__init__(login, password)
        self._work_place = work_place
        self._date_of_birth = date_of_birth
        self._location = location

    def __str__(self):
        return f"{self._login}, {self._work_place} {self._location} {self._date_of_birth} {self._password}"

    def __len__(self):
        print("Len is now working")
        return 0

    def __add__(self, other):
        print(self)
        print(other)
        new_work_place = f"{self._work_place} {other._work_place}"
        new_location = f"{self._location} {other._location}"
        return FaceBookAccount(self._login, self._password, new_work_place, new_location, self._date_of_birth)


def main():
    print('Веедите свои данные')
    login = input("Login ")
    password = input("Password ")
    date_of_birth = input("date_of_birth ")
    work_place = input("Work place ")
    location = input("Location ")
    account = FaceBookAccount(login, password, date_of_birth, work_place, location)
    account2 = FaceBookAccount(login + "2", password, date_of_birth + "2", work_place + "2", location + "2")
    while 1:
        print('Изменить пароль ')
        new_password = input()
        account.password = new_password
        print(account + account2)


main()
