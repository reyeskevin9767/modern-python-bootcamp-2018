import re

# * Example


def extract_phone(input):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    match = phone_regex.search(input)

    if match:
        return match.group()
    return None

# print(extract_phone('My Numer is 432 567-8976'))
# print(extract_phone('My Numer is 432 567-8976d'))
# print(extract_phone('432 567-8976 afsdafads'))
# print(extract_phone('432 567-8976'))


def extract_all_phones(input):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    return phone_regex.findall(input)


# print(extract_all_phones('My Numer is 432 567-8976 or 324 344-2134'))
# print(extract_all_phones('My Numer is 432 567-8976'))


# def is_valid_phone(input):
#     phone_regex = re.compile(r"^\d{3} \d{3}-\d{4}$")
#     match = phone_regex.search(input)

#     if match:
#         return True
#     return False

# print(is_valid_phone("432 567-4543"))
# print(is_valid_phone("432 567-4543 afds"))
# print(is_valid_phone("asdfa 432 567-4543 asdf"))

def is_valid_phone(input):
    phone_regex = re.compile(r"^\d{3} \d{3}-\d{4}$")
    match = phone_regex.fullmatch(input)

    if match:
        return True
    return False


print(is_valid_phone("432 567-4543"))
print(is_valid_phone("432 567-4543 afds"))
print(is_valid_phone("asdfa 432 567-4543 asdf"))
