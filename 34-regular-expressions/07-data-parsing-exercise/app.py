import re

# * Data Parsing Exercise


def parse_date(input):
    name_regex = re.compile(
        r'\b(?P<day>0?[1-9]|[12][0-9]|3[01])(/|.|,)(?P<month>0?[1-9]|1[12])(/|.|,)(?P<year>19[0-9]{2}|[2][0-9][0-9]{2})\b')
    matches = name_regex.search(input)
    if matches:
        return {"d": matches.group('day'), "m": matches.group('month'), "y": matches.group('year')}
    return None


print(parse_date('01,22,1999'))
