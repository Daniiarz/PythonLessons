from utils.classes import Student
from utils.functions import int_input
from utils.settings import IMPORTANT

while 0:
    data = {'course': int_input('Курс'), 'surname': input('Surname '), 'name': input('Name ')}
    student = Student(**data)
    print(student)
    print(IMPORTANT)

a = Student
b = int_input
print(a("surname", "name", 3))


def decorated_function(func):
    def inner_func(*args, **kwargs):
        return f"Result is {func(*args, **kwargs)}!"

    return inner_func


@decorated_function
def a_and_b(num1, num2):
    return num1 + num2


@decorated_function
def a_multiple_b(num1, num2, num3):
    return num1 * num2 * num3


@decorated_function
def return_name():
    return 'Daniiar'


print(a_and_b(99, 90))
print(a_multiple_b(99, 90, num3=90))
print(return_name())