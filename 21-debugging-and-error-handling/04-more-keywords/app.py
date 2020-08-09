
# * try, except, else, finally
# try:
#     num = int(input('Please enter a number: '))
# except:
#     print("That's not a number!")
# else:
#     print("I'm in the else")
# finally:
#     print('Runs No Matter What')

# while True:
#     try:
#         num = int(input('Please enter a number: '))
#     except ValueError:
#         print("That's not a number!")
#     else:
#         print("I'm in the else")
#         break
#     finally:
#         print('Runs No Matter What')

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Don't Divide By Zero")
    except TypeError as err:
        print('a and b must be ints or floats')
        print(err)
    else:
        print(f"{a} divide by {b} is {result}")


print(divide(1, 2))
print(divide(1, 0))
print(divide(1, 'a'))
