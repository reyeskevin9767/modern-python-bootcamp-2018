
# * Lambdas
# * Normal Function
def square(num):
    return num * num

print(square(9))

square2 = lambda num: num * num

add = lambda a,b: a + b

print(square2(9))
print(add(2,4))

# * Lambda
first_lambda = lambda x: x + 5

first_lambda(10) # 15

first_lambda.__name__ # '<lambda>'

# * Lambda
add_values = lambda x, y: x + y

multiply_values = lambda x, y: x + y

add_values(10, 20) # 30

multiply_values(10, 20) # 200