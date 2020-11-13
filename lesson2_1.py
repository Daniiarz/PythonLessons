print("Здарова!!! Че опять деньги потратил?")

expenses = []
while True:
    print("1) Вывести все рассходы ")
    print("2) Сумма всех расходов ")
    print("3) Добавить новый рассход ")
    option = int(input("Выберите вариант: "))
    if option == 3:
        amount = int(input("Введите сумму: "))
        name = input("На что потратил: ")
        date = input("Когда потратил: ")
        expenses.append([amount, name, date])

    if option == 2:
        result = 0
        for rasshod in expenses:
            result += rasshod[0]
        print(f"Сумма ваших рассходов: {result}")

    if option == 1:
        print()
        for rasshod in expenses:
            print(f"{rasshod[0]} | {rasshod[1]} | {rasshod[2]}")
        print()

print("Changes")
