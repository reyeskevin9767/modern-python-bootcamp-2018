
# * Lucky Number 7 Exercise
from random import randint

choice = randint(1, 10)  # Randomly chooses a number between 1 - 10

# * Check to see if choice equals 7
if choice == 7:
    print('lucky')
else:
    print('unlucky')
