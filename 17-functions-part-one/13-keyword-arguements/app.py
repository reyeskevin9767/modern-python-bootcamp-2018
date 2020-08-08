
# * Keyword Arguements
def full_name(first, last):
    return "Your name is {first} {last}"


full_name(first='Colt', last='Steele')  # Your name is Colt Steele

full_name(last='Steele', first='Colt')  # Your name is Colt Steele

# * Keyword Arguements
def full_name2(first="Colt", last="Steele"):
    return "Your name is {first} {last}"


full_name2()  # Your name is Colt Steele

full_name2(last='Enthusiast', first='Python')  # Your name is Python Enthusiast
