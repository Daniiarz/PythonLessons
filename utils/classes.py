class Student:

    def __init__(self, name, surname, course):
        self.name = name
        self.surname = surname
        self.course = course

    def __str__(self):
        return f"{self.name} {self.surname} {self.course}"

    def __repr__(self):
        return self.__str__()
