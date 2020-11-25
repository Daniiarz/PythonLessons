from datetime import datetime


class Expense:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.date = datetime.now()

    def __str__(self):
        return f"{self.name} {self.amount} {self.date}"


expense1 = Expense("Food", 190)


def calc_sum(expenses):
    result = 0
    for expense in expenses:
        result += expense.amount
    return result


def main():
    expenses = []

    while True:
        print("1) Добавить Рассход")
        print("2) Получить Рассходы")
        print("3) Получить Cумму Рассходов")
        print("4) Выход")
        option = int(input("Введите вариант: "))
        if option == 1:
            name = input("Название: ")
            amount = int(input("Сумма: "))
            expenses.append(Expense(name, amount))

        if option == 2:
            for expense in expenses:
                print(expense)

        if option == 3:
            print(calc_sum(expenses))

        if option == 4:
            print("Выход...")
            break

        else:
            print("Выберите один из вариантов!!!!!!!!!")


main()
