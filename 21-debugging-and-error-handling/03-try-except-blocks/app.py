
# * Handle Errors
try:
    foobar
except NameError as err:
    print(err)

# * Handle Errors
try:
    foobar
except:
    print('Problem')
print('After the try')


# * Handle Errors
# Not helpful identifing the problem
try:
    colt
except:
    print("You tried to use a variable that was never declared!")

# * Handle Errors
d = {'name': 'Ricky'}


def get(d, key):
    try:
        d[key]
    except KeyError:
        return None


print(get(d, 'city'))
