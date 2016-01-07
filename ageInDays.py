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
    birthMonth = m1
    days = 0
    
    # Birthday should not be in the future
    if y1 > y2:
        return -1
    if y1 == y2:
        if m1 > m2:
            return -1
        if m1 == m2:
            if d1 > d2:
                return -1
            if d1 == d2:
                return days
    
    # Calculate days between full years
    while y2 - y1 > 1:
        
        isLeap = isLeapYear(y1)
        
        if isLeap == True:
            days = days + leapYearDays
        else:
            days = days + yearDays
            
        y1 = y1 + 1
            
    # Calculate days between months
    # FIXME: Need to account for leap day if it's a leap year
    while m2 != m1: # FIXME: Problem here when the months match
        
        days = days + daysOfMonths[m1 - 1]
        
        if m1 == 12:
            m1 = 1
        else:
            m1 = m1 + 1
        
    # Calculate days between days
    while d2 != d1:
        
        daysInMonth = daysOfMonths[birthMonth - 1]
        days = days + 1
        
        if d1 == daysInMonth:
            d1 = 1
        else:
            d1 = d1 + 1
         
    return days
    
# isLeapYear function verification
# print isLeapYear(2008)
# print isLeapYear(2012)
# print isLeapYear(2016)
# print isLeapYear(2020)
# print isLeapYear(2024)
# print isLeapYear(2028)
# print isLeapYear(2032)
#
# print isLeapYear(2000)
# print isLeapYear(2400)
#
# Not Leap Years
# print isLeapYear(1800)
# print isLeapYear(1900)
# print isLeapYear(2100)
# print isLeapYear(2200)
# print isLeapYear(2300)
# print isLeapYear(2500)

print daysBetweenDates(2019, 4, 6, 2016, 1, 6) # Birthday cannot be in the future
print daysBetweenDates(2012, 1, 1, 2012, 1, 2) # Problem example given. Should = 1
print daysBetweenDates(2015, 1, 1, 2015, 12, 31)
print daysBetweenDates(2015, 1, 1, 2016, 1, 1) # FIXME: This returns 0, which is wrong
print daysBetweenDates(1968, 6, 11, 2016, 1, 7) # FIXME: This is over-calculating days