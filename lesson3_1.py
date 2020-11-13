def print_my_name():
    name = input("Введите имя: ")
    print(name)


def add_a_b(a, b):
    return a + b


result = add_a_b(2, 2)

tasks = []


def add_new_task(tasks):
    task = []
    for i in range(3):
         task.append(input())
    tasks.append(task)


def format_task(task):
    str_result = ""
    for o in task:
        str_result += f"{o} |"
    return str_result


def show_tasks(tasks):
    for i in tasks:
        print(format_task(i))



# while True:
#     print("1) Добавить новое задание")
#     print("2) Показать задания")
#
#     choice = int(input("Выберите вариант "))
#
#     if choice == 1:
#         add_new_task(tasks)
#     if choice == 2:
#         show_tasks(tasks)
#


def name_surname():
    return "Name Surname"


a = name_surname()
if a == "Name Surname":
    print("Есть результат")


def ages(num1, num2):
    return (num1 + num2) / 2


n = ages(18, 19)

if n > 18:
    print(n + 1)
    print("Можете ввойти")

