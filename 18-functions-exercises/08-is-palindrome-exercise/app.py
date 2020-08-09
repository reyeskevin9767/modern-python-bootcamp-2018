
# * Is Palindrome
# def is_palindrome(word):

#     rev_word = word[::-1]
#     if rev_word == word:
#         return True
#     else:
#         return False

def is_palindrome(word):
    """
    >>> is_palindrome('lop')
    False
    """

    rev_word = word[::-1]
    if rev_word == word:
        return True
    else:
        return False
