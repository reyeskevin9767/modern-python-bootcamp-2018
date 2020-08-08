
# * Screaming Repeating Exercise
times = input('How many times do I have to tell you? ')
times = int(times)

# * Version 1
for time in range(times):
    print('CLEAN UP YOUR ROOM')

# One Result
# CLEAN UP YOUR ROOM
# CLEAN UP YOUR ROOM

# *  Version 2
for time in range(times):
    print(f'time {time+1}: CLEAN UP YOUR ROOM')

# One Result
# time 1: CLEAN UP YOUR ROOM
# time 2: CLEAN UP YOUR ROOM
