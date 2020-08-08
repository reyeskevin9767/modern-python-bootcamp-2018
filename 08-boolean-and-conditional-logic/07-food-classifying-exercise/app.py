
# * Food Classifying Exercise
from random import choice

# * Choice randomly chooses a element in list
food = choice(['apple', 'grape', 'bacon', 'steak', 'worm'])

if food == 'apple' or food == 'grape':
    print('fruit')
elif food == 'bacon' or food == 'steak':
    print('meat')
else:
    print('yuck')
