
# * Using Regex
import re

pattern = re.compile(r'\d{3} \d{3}-\d{4}')

# res = pattern.search("Call me at 310 445-9878 or 310 234-5443")
res = pattern.findall("Call me at 310 445-9878 or 310 234-5443")
# print(res.group())
print(res)

res2 = re.search(r'\d{3} \d{3}-\d{4}',
                 "Call me at 310 445-9878 or 310 234-5443").group()

print(res2)
