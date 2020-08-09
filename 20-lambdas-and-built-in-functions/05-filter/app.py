
# * Filter
l = [1, 2, 3, 4]

evens = list(filter(lambda x: x % 2 == 0, l))

evens  # [2,4]

# * Filter
names = ['austin', 'penny', 'anthony', 'angel', 'billy']

a_names = list(filter(lambda n: n[0] == 'a', names))

# * Filter and Map
list(map(lambda name: f"Your instructor is {name}",
         filter(lambda value: len(value) < 5, names)))

# ['Your instructor is Colt']


# * Filter
users = [
    {"username": "samuel", "tweets": [
        "I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]

# extract inactive users using filter:
inactive_users = list(filter(lambda u: not u['tweets'], users))

# extract inactive users using list comprehension:
inactive_users2 = [user for user in users if not user["tweets"]]

# extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(),
                     filter(lambda u: not u['tweets'], users)))

# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]
