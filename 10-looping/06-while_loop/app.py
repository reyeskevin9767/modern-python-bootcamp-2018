
# * While Loops
user_response = None
while user_response != 'please':
    user_response = input("Ah ah ah, you didn't say the magic word: ")

# * Continues to ask for user input until the user types 'bananas'
msg = input('whats the secret password?')
while msg != 'bananas':
    print('WRONG!')
    msg = input('whats the secret password?')
print('CORRECT!')

# * While Loops
# for num in range(1,11):
# 	print(num)

# equivalent of above for loop
num = 1
while num < 11:
    print(num)
    num += 1

print(num)

# Results
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
