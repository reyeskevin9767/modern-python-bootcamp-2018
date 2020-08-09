
# * Exercise
'''
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
'''

# def truncate(string, num):
#     if num < 3:
#         return "Truncation must be at least 3 characters."

#     if (num > len(string) + 2):
#         return string
#     else:
#         print((" ").join(string))
#         return "{}...".format(string[:num - 3])


def truncate(string, n):
    if (n < 3):
        return "Truncation must be at least 3 characters."
    if (n > len(string) + 2):
        return string

    return string[:n - 3] + "..."


print(truncate("Problem solving is the best!", 10))
