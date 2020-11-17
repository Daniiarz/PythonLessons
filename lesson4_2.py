from datetime import date
from random import randint


def write_to_file(line):
    new_file = open("score_board.txt", "a")
    new_file.write(f"{line}\n")
    new_file.close()


def read_from_file():
    file = open("score_board.txt", "r")
    lines = file.readlines()
    file.close()
    return lines


def int_input(text):
    while True:
        try:
            return int(input(f"Введите ваше {text} "))
        except Exception:
            print(f"Введите ваш {text} ввиде числа ")


def game(nickname):
    start = 0
    end = 21
    random_num = randint(start, end)

    for i in range(5):
        user_num = int_input(f"Число от {start} до {end - 1}")
        if user_num == random_num:
            print(f"Вы выиграли! кол-во {i + 1}")
            write_to_file(f"{nickname}|{date.today()}|{i+1}")
            break
        else:
            if random_num - 3 < user_num < random_num + 3:
                print("Горячо")

            elif random_num - 5 < user_num < random_num + 5:
                print("Холодно")

            print("Попробуйте еще раз!")

    print(f"Вы проиграли число было - {random_num}")


def main():
    nickname = input("Введиет ваш никнейм: ")
    while True:
        print("1) Начать игру")
        print("2) Список лидеров")
        print("3) Выйти из игры")
        option = int_input("Вариант")

        if option == 1:
            game(nickname)

        if option == 2:
            lines = read_from_file()
            for i in lines:
                print(i)

        if option == 3:
            break


main()
