class House:


    def __init__(self, address, elevator, flats, floors=5, sixth_floor=None):
        print("Initialization")
        self.floors = floors
        self.address = address
        self.elevator = elevator
        self.flats = flats
        self.sixth_floor = sixth_floor
        self.rented = False


    def give_to_rent(self):
        self.rented = True
        return f"Дом {self.address}/{self.floors}/{self.sixth_floor} сдан в аренду"

    def fun(self):
        return "Text"


hryshevka = House("Токтогула 175", False, 100)
hryshevka2 = House("Манаса 61", True, 200, 9, True)

print(f"Этажи ? => {hryshevka.floors}")
print(f"Адресс ? => {hryshevka.address}")
print(f"Лифт ? => {hryshevka.elevator}")
print(f"Квартиры ? => {hryshevka.flats}")
print(f"Шестой этаж ? => {hryshevka.sixth_floor}")
print(f"Арендовано ? => {hryshevka.rented}")


print()
print(f"Этажи ? => {hryshevka2.floors}")
print(f"Адресс ? => {hryshevka2.address}")
print(f"Лифт ? => {hryshevka2.elevator}")
print(f"Квартиры ? => {hryshevka2.flats}")
print(f"Шестой этаж ? => {hryshevka2.sixth_floor}")
print(f"Арендовано ? => {hryshevka2.rented}")

print(hryshevka.give_to_rent())
print(hryshevka2.give_to_rent())
print(hryshevka.fun())
print()
print(f"Арендовано ? => {hryshevka.rented}")
print(f"Арендовано ? => {hryshevka2.rented}")
