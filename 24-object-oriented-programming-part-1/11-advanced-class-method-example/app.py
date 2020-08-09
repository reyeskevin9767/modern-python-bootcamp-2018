
# * Advanced Class Method Example
class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th. {self.first}"

    def say_hi(self):
        return "Hi"


# print(User.active_users)
# user1 = User("Joey", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.active_users)
# print(user2.logout())
# print(user1.full_name())
# print(user2.full_name())
# print(user1.initials())
# print(user2.likes("Ice Cream"))
# print(user2.birthday())
# print(User.active_users)

# print(User.display_active_users())
# user1 = User("Joey", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.display_active_users())


tim = User.from_string("Tim,Jones,89")

print(tim.full_name())
