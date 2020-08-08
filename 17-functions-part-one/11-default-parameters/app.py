
# * Default Parameters
def add(a=10, b=20):
    return a+b


add()  # 30
add(1, 10)  # 11


# * Default Parameters
def exponent(num, power=2):
    return num ** power


print(exponent(2, 3))  # 8
print(exponent(3))  # 9
print(exponent(7))  # 49


# * Default Parameters
def show_information(first_name="Colt", is_instructor=False):
    if first_name == "Colt" and is_instructor:
        return "Welcome back instructor Colt!"
    elif first_name == "Colt":
        return "I really thought you were an instructor..."
    return f"Hello {first_name}!"


show_information()  # "I really thought you were an instructor..."
show_information(is_instructor=True)  # "Welcome back instructor Colt!"
show_information('Molly')  # Hello Molly!

# * Default Parameters


def add2(a, b):
    return a+b


def math(a, b, fn=add2):
    return fn(a, b)


def subtract(a, b):
    return a-b


math(2, 2)  # 4

math(2, 2, subtract)  # 0
