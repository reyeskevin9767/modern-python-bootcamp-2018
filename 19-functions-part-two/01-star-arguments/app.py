
# * (* args)
# def sum_all_nums(num1,num2,num3):
#     return num1 + num2 + num3
def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_all_nums(3, 4, 5))


def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"

    return "Not sure who you are..."


ensure_correct_info()  # Not sure who you are...

ensure_correct_info(1, True, "Steele", "Colt")
