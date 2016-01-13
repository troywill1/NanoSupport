###
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

    # If the day is not 30, then we can safely increment the day and return,
    # as we are not going to need to increment the month or year since
    # we are not at the end of the month.
    if day < 30:

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
# daysBetweenDates function. I will write a fucntion to verify that the
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
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3),
                  ((2013,1,1,1999,12,31), "AssertionError")]

    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print "Test with data:", args, "failed"
            else:
                print "Test case passed!"
        except AssertionError:
            if answer == "AssertionError":
                print "Nice job! Test case {0} correctly raises AssertionError!\n".format(args)
            else:
                print "Check your work! Test case {0} should not raise AssertionError!\n".format(args)
test()
