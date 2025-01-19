#build sentaific calender

import calendar
import datetime

def caladd(year, month, day, add):
    c = calendar.Calendar()
    for i in c.itermonthdays(year, month):
        if i == day:
            d = datetime.date(year, month, i)
            print(d + datetime.timedelta(days=add))
            break
    else:
        print('Invalid day')

caladd(2019, 2, 28, 1)