# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.
 
daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 
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
    
    birthYear = y1
    birthMonth = m1
    birthDay = d1
    currentYear = y2
    currentMonth = m2
    currentDay = d2
    
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
    while currentYear - birthYear > 1:
        
        isLeap = isLeapYear(birthYear)
        
        if isLeap == True:
            days = days + leapYearDays
        else:
            days = days + yearDays
            
        birthYear += 1
            
    # Calculate days between months
    if (m1 == m2) & (y1 != y2):
        monthCounter = 0
        
        while monthCounter < 12:
            days += daysOfMonths[birthMonth - 1]
            monthCounter += 1
            birthMonth += 1
            
        isLeap = isLeapYear(y1)
        if (isLeap == True) & (m1 != 2):
            days += 1
        
        isLeap = isLeapYear(y2)
        if (isLeap == True) & (m2 > 2):
            days += 1
            
    elif (m1 < m2) & (y1 != y2):
        monthCounter = 0
        plusMonths = (m2 - m1) + 12

        while monthCounter < plusMonths:
            
            days += daysOfMonths[birthMonth - 1]
            monthCounter += 1
            
            if birthMonth == 12:
                birthMonth = 1
            else:
                birthMonth += 1
                 
        isLeap = isLeapYear(y1)
        if (isLeap == True) & (m1 != 2):
            days += 1
        
        isLeap = isLeapYear(y2)
        if (isLeap == True) & (m2 > 2):
            days += 1
            
    else:
        
        while currentMonth != birthMonth:
            
            days += daysOfMonths[birthMonth - 1]
        
            if birthMonth == 12:
                birthMonth = 1
            else:
                birthMonth += 1
        
    # Calculate days between days
    birthMonth = m1 # Reset birthMonth variable back to m1 as it may have changed
    while currentDay != birthDay:
        
        daysInMonth = daysOfMonths[birthMonth - 1]
        days += 1
        
        if birthDay == daysInMonth:
            birthDay = 1
        else:
            birthDay += 1
        
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

# print daysBetweenDates(2019, 4, 6, 2016, 1, 6) # Birthday cannot be in the future, -1
print daysBetweenDates(2012, 1, 1, 2012, 1, 2) # Problem example given. Should = 1
# print daysBetweenDates(2015, 1, 1, 2015, 12, 31) # 364
# print daysBetweenDates(2015, 1, 1, 2016, 1, 1) # 365
# print daysBetweenDates(2014, 1, 1, 2015, 1, 1) # 365
# print daysBetweenDates(2016, 1, 1, 2017, 1, 1) # 366
# print daysBetweenDates(2015, 1, 1, 2016, 3, 1) # 425
# print daysBetweenDates(2013, 1, 1, 2016, 1, 8) # 1102
# print daysBetweenDates(1968, 6, 11, 2016, 1, 7) # FIXME: This is over-calculating days