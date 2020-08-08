
# * Global
total = 0

def increment():
    global total
    total += 1
    return total

increment() # 

# * Global
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()

