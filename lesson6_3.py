class Vehicle:

    def __init__(self, serial_number, year_of_production, country, gear_type):
        self.number = serial_number
        self.year_of_production = year_of_production
        self.country = country
        self.gear_type = gear_type

    @property
    def serial_number(self):
        return self.number

    @serial_number.setter
    def serial_number(self, value):
        print(value)
        print("Serial number can't be changed")


class Sedan(Vehicle):
    def __init__(self, serial_number, year_of_production, country, gear_type, is_4placed):
        super(Sedan, self).__init__(serial_number, year_of_production, country, gear_type)
        self.is_4placed = is_4placed


class Tank(Vehicle):
    def __init__(self, serial_number, year_of_production, country, gear_type, armour):
        super(Tank, self).__init__(serial_number, year_of_production, country, gear_type)
        self.armour = armour


class Boat(Vehicle):
    def __init__(self, serial_number, year_of_production, country, gear_type, is_parus):
        super(Boat, self).__init__(serial_number, year_of_production, country, gear_type)
        self.is_parus = is_parus


a = Boat(123012341234, 2020, "Kg", "manual", False)
a.serial_number = 123
print(a.serial_number)