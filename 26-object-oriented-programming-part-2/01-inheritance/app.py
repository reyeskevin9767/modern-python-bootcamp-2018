
# * Inheritance
class Animal:
    cool = True

    def make_sound(self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):
    pass


a = Animal()
a.make_sound("Chirp")

blue = Cat()
blue.make_sound("Meow")
print(blue.cool)

print(isinstance(blue, object))
