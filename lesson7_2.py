class Drob:

    def __init__(self, chilitel, znamentel):
        self.chilitel = chilitel
        self.znamentel = znamentel

    def __mul__(self, other):
        new_chilitel = self.chilitel * other.chilitel
        new_znamentel = self.znamentel * other.znamentel

        return Drob(new_chilitel, new_znamentel)

    def __str__(self):
        return f"{self.chilitel}\n{max(len(str(self.znamentel)), len(str(self.chilitel))) * '-'}\n{self.znamentel}"


drob1 = Drob(20, 6)
drob2 = Drob(3, 9)
drob3 = drob1 * drob2
drob4 = drob3 * drob1
print(drob4)
