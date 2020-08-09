
# * Exercise
'''
counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1 
'''

# def letter_counter(string):
#     def inner(let):
#         letter_counter.accumulator = 0
#         for letter in string.lower():
#             if letter == let:
#                 letter_counter.accumulator += 1
#         return letter_counter.accumulator


#     return inner


def letter_counter(s):
    letter_counter.val = s

    def inner(char):
        return len(list(c.lower() for c in letter_counter.val.lower() if c == char))
    return inner


counter = letter_counter('Amazing')
print(counter('a'))  # 2

counter2 = letter_counter('This Is Really Fun!')
print(counter2('i'))  # 2
print(counter2('t'))  # 1
