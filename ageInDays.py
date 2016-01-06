# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.
 
daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 
def isLeapYear(year):
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
        
    return True
    
 
def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    ##
    # Your code here.
    ##
    yearDays = 365
    leapYearDays = 366
    days = 0
    
    while y2 - y1 > 1:
        
        year = y1 + 1 # Fix here, year never checked, counter doesn't work
        isLeap = isLeapYear(year)
        
        if isLeap == True:
            days = days + leapYearDays
        else:
            days = days + yearDays
            
    return days
    
# isLeapYear function verification
print isLeapYear(2008)
print isLeapYear(2012)
print isLeapYear(2016)
print isLeapYear(2020)
print isLeapYear(2024)
print isLeapYear(2028)
print isLeapYear(2032)

print isLeapYear(2000)
print isLeapYear(2400)

# Not Leap Years
print isLeapYear(1800)
print isLeapYear(1900)
print isLeapYear(2100)
print isLeapYear(2200)
print isLeapYear(2300)
print isLeapYear(2500)

print daysBetweenDates(1968, 6, 11, 2016, 1, 6)