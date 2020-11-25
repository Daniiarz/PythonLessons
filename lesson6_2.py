class Country:

    def __init__(self, name, territory, population, language):
        self._name = name
        self.territory = territory
        self.population = population
        self.language = language

    def __str__(self):
        return f"{self.name} {self.territory} {self.population} {self.language}"

    def live(self):
        return self.population

    @property
    def get_beautiful_country(self):
        return "Lol"

    @property
    def name(self):
        # print("Here is a functions")
        return self._name

    @name.setter
    def name(self, value):
        if type(value) != str:
            print('Inncorect type!!!')
        else:
            self._name = value

class Region(Country):

    def __init__(self, country, region_name, region_territory, region_population):
        super(Region, self).__init__(country.name, country.territory, country.population, country.language)
        self.region_name = region_name
        self.region_territory = region_territory
        self.region_population = region_population

    def __str__(self):
        return f"{super(Region, self).__str__()} {self.region_name} {self.region_territory} {self.region_population}"

    def live(self):
        return super(Region, self).live() - self.region_population


country = Country("Kyrgyzystan", 10923741029374, 6000000, "kyrgyz")
talas = Region(country, "Talas", 1289999930012384, 1)
chuy = Region(country, "Chuy", 912039741094, 12093710923)
yssyk_kol = Region(country, "Yssyk-Kol", 130942031234,
                   19283741)
osh = Region(country, "Osh", 1238974102, 12301234123)

print(talas.name)
print(chuy.name)
print(yssyk_kol.name)
yssyk_kol.name = 18098
print(yssyk_kol.name)
print(osh.get_beautiful_country)
print(country.live())
print(osh.live())
