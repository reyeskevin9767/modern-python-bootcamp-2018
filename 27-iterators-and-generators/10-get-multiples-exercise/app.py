
# * Get Multiple Exercise
# def get_multiples(num = 1, count = 10):
#     start_num = 0
#     while True:
#         if count > 0:
#             start_num += num
#             yield start_num
#             count -= 1
#         else:
#             raise StopIteration

def get_multiples(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num


evens = get_multiples(2, 3)

print(next(evens))
print(next(evens))
print(next(evens))
