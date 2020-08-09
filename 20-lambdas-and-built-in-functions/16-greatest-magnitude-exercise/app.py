
# * Greatest Magnitude Exercise
def max_magnitude(num):
    new_num = [abs(x) for x in num]
    return max(new_num)
