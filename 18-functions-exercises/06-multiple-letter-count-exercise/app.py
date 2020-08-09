

# * Multiple Letter Count
# def multiple_letter_count(string):

#     return {x : string.count(x) for x in string}

def multiple_letter_count(string):
    """
    >>> multiple_letter_count('lol')
    {'l': 2, 'o': 1}
    """

    return {x: string.count(x) for x in string}
