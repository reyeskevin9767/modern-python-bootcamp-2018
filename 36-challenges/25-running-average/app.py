
# * Exercise
'''
rAvg = running_average()
rAvg(10) # 10.0
rAvg(11) # 10.5
rAvg(12) # 11

rAvg2 = running_average()
rAvg2(1) # 1
rAvg2(3) # 2
'''

# def running_average():
#     running_average.sum = 0
#     running_average.counter = 0
#     def run_avg(num):
#         running_average.sum += num
#         running_average.counter += 1
#         return running_average.sum / running_average.counter

#     return run_avg


def running_average():
    running_average.accumulator = 0
    running_average.size = 0

    def inner(number):
        running_average.accumulator += number
        running_average.size += 1
        return running_average.accumulator / running_average.size

    return inner


rAvg = running_average()
print(rAvg(10))
print(rAvg(11))
print(rAvg(12))
