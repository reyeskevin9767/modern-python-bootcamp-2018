
# * Open File
file = open("story.txt")
file.read()
file.close()

file.closed  # True

# * Open File (Best Way)
with open("story.txt") as file:
    file.read()

file.closed  # True
