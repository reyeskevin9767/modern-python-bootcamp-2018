
# * Chicken Coop Exercise
class Chicken:

    total_eggs = 0

    def __init__(self, name, species, eggs=0):
        self.name = name
        self.species = species
        self.eggs = eggs

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs


c1 = Chicken(name="Alice", species="Partridege Sikie")
c2 = Chicken(name="Alice2", species="Partridege Sikie2")
print(Chicken.total_eggs)
print(c1.lay_egg())
print(Chicken.total_eggs)
print(c2.lay_egg())
print(c2.lay_egg())
print(Chicken.total_eggs)
