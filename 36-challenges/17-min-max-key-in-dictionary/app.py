
# * Exercise
'''
min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}) # [1,4]
'''

# def min_max_key_in_dictionary(dict_1):

#     key_max = max(x for x in dict_1.values() for x in dict_1.keys())
#     key_min = min(x for x in dict_1.values() for x in dict_1.keys())

#     return [key_min, key_max]


def min_max_key_in_dictionary(d):
    keys = d.keys()
    return [min(keys), max(keys)]


print(min_max_key_in_dictionary({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}))
