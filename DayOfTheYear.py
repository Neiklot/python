def isYearLeap(year):
    if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
        return True
    return False

def daysInMonth(year, month):
    daysInMonths=[None,31,28,31,30,31,30,31,31,30,31,30,31]
    if isYearLeap(year) and month==2:
        return daysInMonths[month]+1
    else:
        return daysInMonths[month]

def checkValues(year, month, day):
    if year < 1582 or month < 1 or month > 12 or day < 1 or day > daysInMonth(year, month):
        return None
    return True

def dayOfYear(year, month, day):
    if checkValues(year,month,day)==None:
       return None
    totalDays=0;
    for i in range(1,month):
        totalDays+=daysInMonth(year,i)
    return totalDays+day

print(dayOfYear(2000, 12, 31))
print(dayOfYear(1983, 12, 3))
print(dayOfYear(2010, 5, 28))