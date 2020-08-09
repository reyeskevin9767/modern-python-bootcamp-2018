import re

# * Regex Exercise


def censor(text):
    pattern = re.compile(r'\b(frack|fracking)\b', re.I)
    result = pattern.sub(r"CENSORED", text)
    return result


# import re

# def censor(input):
#     pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
#     return pattern.sub("CENSORED", input)

print(censor("Fracking You"))
