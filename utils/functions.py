def int_input(text):
    while True:
        try:
            return int(input(f"Введите ваше {text} "))
        except Exception:
            print(f"Введите ваш {text} ввиде числа ")
