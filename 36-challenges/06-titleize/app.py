
# * Exercise
'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''

# def titleize(sentence):
#     split_sentence = sentence.split(" ")
#     new_sentence = []
#     for word in split_sentence:
#        new_sentence.append("{}{}".format(word[:1].upper(), word[1::]))

#     return (" ").join(new_sentence)


def titleize(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))


print(titleize('this is awesome'))
