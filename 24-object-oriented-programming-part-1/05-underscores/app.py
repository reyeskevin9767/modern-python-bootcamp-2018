
# * Underscores
class Person:
    def __init__(self):
        self.name = 'Tony'
        self._secret = 'hi'
        self.__msg = "I like turtles"
        self.__lol = "HAHHAHAHAH"

    def doorman(self, guess):
        if guess == self._secret:
            print("Let Them IN")


p = Person()

print(p.name)
print(p._secret)        # Interal Use Only
print(p._Person__msg)  # Changes name to put class name first
print(p._Person__lol)
