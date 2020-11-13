def int_input(text):
    while True:
        try:
            return int(input(f"Введите ваш {text} "))
        except Exception:
            print(f"Введите ваш {text} ввиде числа ")



def input_initial_data():
    name = input("Введите ваше имя ")
    surname = input("Введите вашу фамилию ")
    age = int_input("Возраст")
    if age < 18:
        return None

    return f"{name}, {surname}, {age}"


def main():
    secret_num = 20
    player = input_initial_data()
    if player is None:
        print("Вам незлья. Нужен родительския контроль!!!!!!!!!!")
        return
    print(f"Привет {player}!")

    for i in range(5):
        num = int_input("Число")
        if num == secret_num:
            print(f"Вы угадали ! Секретное число {secret_num}. Попыток было сделанно {i+1}")
            return


main()