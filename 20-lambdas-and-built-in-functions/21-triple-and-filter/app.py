
# * Triple And Filter
def triple_and_filter(num):
    return [x * 3 for x in list(filter(lambda x: x % 4 == 0, num))]


num = [2, 3, 4, 5, 6]

print(triple_and_filter(num))
