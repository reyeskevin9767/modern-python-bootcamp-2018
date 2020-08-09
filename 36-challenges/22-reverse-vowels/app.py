
# * Exercise
'''
reverse_vowels("Hello!") # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''

# def reverse_vowels(string):
#     reverse_string = []
#     vowels = []
#     idx = 0


#     for x in string:
#         if x.lower() in "aeiou":
#             vowels.append(x)

#     reverse_vowels = vowels[::-1]

#     for x in string:
#         if x.lower() in "aeiou":
#             x = reverse_vowels[idx]
#             reverse_string.append(x)
#             idx += 1
#         else:
#             reverse_string.append(x)
#     return "".join(reverse_string)

def reverse_vowels(s):
    vowels = "aeiou"
    string = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
    return "".join(string)


print(reverse_vowels("Reverse Vowels In A String"))
