# Your imports
from datetime import *
from calendar import month_name

def months_interval(start_date, end_date):
    month_lookup = list(month_name)
    start_date = start_date.replace(day = 1)
    end_date = end_date.replace(day = 1)
    months_str = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December']
    months = []
    while start_date <= end_date:
        month = start_date.month
        year  = start_date.year
        month_str = months_str[month-1]
        months.append("{0}".format(month_str))
        next_month = month+1 if month != 12 else 1
        next_year = year + 1 if next_month == 1 else year
        start_date = start_date.replace( month = next_month, year= next_year)
    res=[]
    [res.append(x) for x in months if x not in res]
    return sorted(res, key=month_lookup.index)