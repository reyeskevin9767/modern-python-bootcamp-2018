
# * Number is Odd Exercise
from random import randint

num = randint(1, 1000)  # Randomly generators a number between 1 - 1000

# * Checks if num when module by 2 equals 0
if num % 2 != 0:
    print('odd')
else:
    print('even')
