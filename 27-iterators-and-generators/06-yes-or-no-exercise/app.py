
# * Yes Or No Exercise
# def yes_or_no():
# 	answer = True
# 	while True:
# 		if answer == True:
# 			answer = False
# 			yield 'yes'
# 		else:
# 			answer = True
# 			yield "no"

def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"


yes = yes_or_no()

print(next(yes))
print(next(yes))
print(next(yes))
