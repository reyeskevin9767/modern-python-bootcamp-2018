
# * Unlucky Numbers Exercise

# * Solution
for num in range(1, 21):
    if num == 4 or num == 13:
        print(f'{num} is unlucky')
    elif num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

# Results
# 1 is odd
# 2 is even
# 3 is odd
# 4 is unlucky
# 5 is odd
# 6 is even
# 7 is odd
# 8 is even
# 9 is odd
# 10 is even
# 11 is odd
# 12 is even
# 13 is unlucky
# 14 is even
# 15 is odd
# 16 is even
# 17 is odd
# 18 is even
# 19 is odd
# 20 is even

# * Refactor
for num in range(1, 21):
    if num == 4 or num == 13:
        state = 'unlucky'
    elif num % 2 == 0:
        state = 'even'
    else:
        state = 'odd'
    print(f'{num} is {state}')


# Results
# 1 is odd
# 2 is even
# 3 is odd
# 4 is unlucky
# 5 is odd
# 6 is even
# 7 is odd
# 8 is even
# 9 is odd
# 10 is even
# 11 is odd
# 12 is even
# 13 is unlucky
# 14 is even
# 15 is odd
# 16 is even
# 17 is odd
# 18 is even
# 19 is odd
# 20 is even
