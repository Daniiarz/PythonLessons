def sum_of_numbers(a, b, *args, **kwargs):  # *args, **kwargs -> key word
    print(type(args))
    print(len([*args]))
    print(a)
    print(b)
    print()
    return sum(args)


name_surname = {'a': "Daniiar", 'b': "M"}


class Student:

    def __init__(self, name, surname, course):
        self.name = name
        self.surname = surname
        self.course = course

    def __str__(self):
        return f"{self.name} {self.surname} {self.course}"

    def __repr__(self):
        return self.__str__()


students = []

while 1:
    data = [input("Course: "), input("Name: "), input("Surname: ")]
    data2 = {'course': input("Course: "), 'name': input("Name: "), 'surname': input("Surname: ")}
    student = Student(*data)
    student2 = Student(**data2)
    students.append(student2)
    students.append(student)
    print(student)
    print(student2)
    print(students)
