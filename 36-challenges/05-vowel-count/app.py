
# * Exercise
'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''

# def vowel_count(word):
#     lower_case_word = word.lower()
#     new_word = [char for char in lower_case_word if char in "aeiou"]
#     dict_words = {}
#     for word in new_word:
#         if word not in dict_words:
#             dict_words[word] = 1
#         else:
#             dict_words[word] += 1
#     return dict_words


def vowel_count(string):
    lower_s = string.lower()
    return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}


print(vowel_count('Elie'))
