
# * Open file and read and write into file
# with open("haiku.txt", "w") as file:
#     file.write("Writing files is great\n")
#     file.write("Here's another line of text\n")
#     file.write("Closing now, goodbye!")

# with open("haiku.txt", "a") as file:
#     file.write("Writing files is great\n")
#     file.write("Here's another line of text\n")
#     file.write("Closing now, goodbye!")

with open("haiku.txt", "r+") as file:
    file.write("Closing now, adfasdfadsfgoodbye! maybe")
    file.seek(10)
    file.write(":(")
