
# * Exercise
'''
valid_parentheses("()") # True 
valid_parentheses(")(()))") # False 
valid_parentheses("(") # False 
valid_parentheses("(())((()())())") # True 
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''

# def valid_parentheses(string):
#     if len(string) % 2 != 0:
#         return False

#     result = "".join(string.split("()"))
#     if result == string:
#         return string == ""
#     return valid_parentheses(result)


def valid_parentheses(parens):
    count = 0
    i = 0
    while i < len(parens):
        if (parens[i] == '('):
            count += 1
        if (parens[i] == ')'):
            count -= 1
        if (count < 0):
            return False
        i += 1
    return count == 0


print(valid_parentheses("()"))
print(valid_parentheses(")(()))"))
print(valid_parentheses("("))
print(valid_parentheses('))(('))
print(valid_parentheses('))(('))
