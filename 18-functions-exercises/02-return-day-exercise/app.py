
# * Return Day
# def return_day(num):
#     week_days = {
#         1: 'Sunday',
#         2: 'Monday',
#         3: 'Tuesday',
#         4: 'Wednesday',
#         5: 'Thursday',
#         6: 'Friday',
#         7: 'Saturday',
#     }
#     if num in week_days:
#         return week_days[num]
#     else:
#         return None

def return_day(num):
    """
    >>> return_day(1)
    'Sunday'

    >>> return_day(2)
    'Monday'
    """
    week_days = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday',
    }
    if num in week_days:
        return week_days[num]
    else:
        return None
