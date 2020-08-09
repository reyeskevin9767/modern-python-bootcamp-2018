
# * Get Unlimited Multiples
def get_unlimited_multiples(num=1):
    next_num = 0
    while True:
        next_num += num
        yield next_num


ones = get_unlimited_multiples()

print([next(ones) for i in range(20)])
