# I coded this solution myself as I worked thorough the video lessons in
# the "2.7 How to Solve Problems section."

# I already coded this solution in the file "ageInDays.py" prior to
# watching the lesson.

# I did make some changes to my code here based on the lessons, but I was
# able to work through everything without having to go to the videos for the
# answer.

# I learned alot about breaking things up into smaller, simple, more
# manageable pieces. This solution took much less time to write and is
# easier read and understand.
#
# -Troy

# This is much more clear, concise and elegant than my solution in
# 'ageInDays.py'.
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):

    """Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days."""

    # YOUR CODE HERE

    # How many days are in the month?
    numOfDays = daysInMonth(year, month)

    # If the day is not 30, then we can safely increment the day and return,
    # as we are not going to need to increment the month or year since
    # we are not at the end of the month.
    if day < numOfDays:

        return year, month, day + 1

    # Since day is 30 and the month is 12, this is the end of the year.
    # increment the year and set the month and day to 1.
    elif month == 12:

        return year + 1, 1, 1

    # Since the day is 30 and the month is not 12, we need to increment the
    # month and set the day to 1.
    return year, month + 1, 1

# Test the nextDay function

# print nextDay(1999, 12, 30)
# print nextDay(2013, 1, 30)
# print nextDay(2012, 12, 30)


# The video instructions asked to write a helper function to the
# daysBetweenDates function. I will write a function to verify that the
# first date is not after the second.

def dateIsBefore(year1, month1, day1, year2, month2, day2):

    """Returns True if the first date is prior to the second
    date, otherwise, it returns False"""

    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
                return day1 < day2

    return False

# Finish the lesson by writing and utilizing the helper functions
# daysInMonth and isLeapYear.

def daysInMonth(year, month):

    """Given the year and month, returns the number of days in the month"""

    daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # If the month is February, check to see if the year is a Leap Year and
    # return the correct number of days.
    if month == 2:
        isLeap = isLeapYear(year)
        if isLeap:
            return 29
        return 28

    return daysOfMonths[month - 1]

def isLeapYear(year):

    """Given the year, returns True if the year is a Leap Year, otherwise,
    returns False"""

    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False

    return True

# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):

    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    # YOUR CODE HERE!
    # Add an assertion to make sure the input dates are valid.
    assert dateIsBefore(year1, month1, day1, year2, month2, day2)

    days = 0

    # If the first date is not after the second date, start counting days.
    # Increment days until the first date is not before the second date.
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1

    return days


# Testing script
def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
            print result
        else:
            print "Test case passed!"

test()

# Save this test script as an example of using try/except
# def test():
    # test_cases = [((2012,9,30,2012,10,30),30),
                #   ((2012,1,1,2013,1,1),360),
                #   ((2012,9,1,2012,9,4),3),
                #   ((2013,1,1,1999,12,31), "AssertionError")]

    # for (args, answer) in test_cases:
        # try:
            # result = daysBetweenDates(*args)
            # if result != answer:
                # print "Test with data:", args, "failed"
                # print result
            # else:
                # print "Test case passed!"
                # print result
        # except AssertionError:
            # if answer == "AssertionError":
                # print "Nice job! Test case {0} correctly raises AssertionError!\n".format(args)
            # else:
                # print "Check your work! Test case {0} should not raise AssertionError!\n".format(args)
# test()
