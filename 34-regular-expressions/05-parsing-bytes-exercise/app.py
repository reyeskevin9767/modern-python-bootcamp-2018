# import re

# def parse_bytes(input):
#     pattern = re.compile(r'\b\d{8}\b')
#     match = pattern.findall(input)
#     return match

# * Parsing Exercise
import re


def parse_bytes(input):
    binary_regex = re.compile(r'\b[10]{8}\b')
    results = binary_regex.findall(input)
    return results


print(parse_bytes('adsfdas'))
