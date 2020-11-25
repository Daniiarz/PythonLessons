class Human:
    def __init__(self, name, surname, age, weight):
        self.name = name
        self.surname = surname
        self.age = age
        self.weight = weight

    def __str__(self):
        return f"{self.name} {self.surname} {self.age} {self.weight}"

    def live(self):
        return "Ok"

    def get_name(self):
        return self.name


class Citizen(Human):

    def __init__(self, name, surname, age, weight, country):
        super(Citizen, self).__init__(name, surname, age, weight)
        self.country = country


class Student(Citizen):

    def __init__(self, name, surname, age, weight, country, university, faculty, course):
        super(Student, self).__init__(name, surname, age, weight, country)
        self.university = university
        self.course = course
        self.faculty = faculty

    def get_university(self):
        return f"{self.country} {self.university}"


student = Student("Daniiar", "M", 19, 62, "Kyrgyzystan", "Ala-Too", "CS", 3)
print(student.get_name())
print(student.country)
print(student.surname)
print(student.get_university())
