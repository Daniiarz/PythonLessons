def write_to_file(line):
    new_file = open("text.txt", "a")
    new_file.write(f"{line}\n")
    new_file.close()


def read_from_file():
    file = open("text.txt", "r")
    lines = file.readlines()
    file.close()
    return lines


def calc_sum():
    lines = read_from_file()
    result = 0
    for i in lines:
        line = i.split("|")
        amount = int(line[1])
        result += amount
    return result

def main():
    while True:
        print("1) Добавить Рассход")
        print("2) Получить Рассходы")
        print("3) Получить Cумму Рассходов")
        print("4) Выход")
        option = int(input("Введите вариант: "))
        if option == 1:
            name = input("Название: ")
            amount = input("Сумма: ")
            date = input("Дата: ")
            write_to_file(f"{name}|{amount}|{date}")

        if option == 2:
            lines = read_from_file()
            for i in lines:
                print(i)

        if option == 3:
            print(calc_sum())

        if option == 4:
            print("Выход...")
            break

        else:
            print("Выберите один из вариантов!!!!!!!!!")

main()
