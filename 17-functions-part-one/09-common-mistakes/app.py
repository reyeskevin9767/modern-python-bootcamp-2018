
# * Common Mistakes
# * Old Version
def sum_odd_numbers1(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
        return total  # Returning too early


# * New Version
def sum_odd_numbers2(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total


print(sum_odd_numbers1([1, 2, 3, 4, 5, 6, 7]))

print(sum_odd_numbers2([1, 2, 3, 4, 5, 6, 7]))

# * Old Version


def is_odd_number1(num):
    if num % 2 != 0:
        return True
    else:  # This else is unnecessary
        return False

# * New Version


def is_odd_number2(num):
    if num % 2 != 0:
        return True
    return False  # We can just return without the else


print(is_odd_number1(4))
print(is_odd_number2(9))
