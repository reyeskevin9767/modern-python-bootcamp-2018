# import re

# def is_valid_time(time):
#     time_regex = re.compile(r"\A\b\d{1,2}:\d{2}\b")
#     match = time_regex.search(time)

#     if match:
#         return True
#     else:
#         return False

# * Example
import re


def is_valid_time(input):
    pattern = re.compile(r'^\d\d?:\d\d$')
    match = pattern.search(input)
    if match:
        return True
    return False


print(is_valid_time("10:45"))
print(is_valid_time("1:23"))
print(is_valid_time("10.45"))
print(is_valid_time("1999"))
print(is_valid_time("145.23"))
print(is_valid_time("it is 13:15"))
