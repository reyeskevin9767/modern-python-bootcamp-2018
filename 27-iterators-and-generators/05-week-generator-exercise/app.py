
# * Week Generator Exercise
def week():
    days = ('Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday')
    for day in days:
        yield day


week = week()

print(next(week))
print(next(week))
print(next(week))
print(next(week))
print(next(week))
print(next(week))
print(next(week))
