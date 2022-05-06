from datetime import *
def myFunction(dt1,dt2):
    date1 = datetime.strptime(dt1, "%Y-%m-%d")
    date2 = datetime.strptime(dt2, "%Y-%m-%d")
    date1 = date1.replace(day = 1)
    date2 = date2.replace(day = 1)
    months_str = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']
    months = []
    while date1 <= date2:
        month = date1.month
        year  = date1.year
        month_str = months_str[month-1]
        months.append("{0}".format(month_str))
        next_month = month+1 if month != 12 else 1
        next_year = year + 1 if next_month == 1 else year
        date1 = date1.replace( month = next_month, year= next_year)
    return months
monthsArray = myFunction("2020-01-01","2020-12-11")
print(monthsArray)