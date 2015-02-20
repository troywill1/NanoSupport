# Introduction to Serious Programming - First Programming Quiz

# Write a Python program that prints out the number of minutes in seven weeks.

print (24 * 60) * 7 * 7

# Introduction to Serious Programming - Speed of Light

# Write Python code to print how far light travels in centimeters in one nanosecond.
# Use the values below:
# speed_of_light = 299792458 	meters per second
# centimeters = 100				one meter is 100 centimeters
# nanosecond = 1.0/1000000000	one billionth of a second

print 299792458 * (1.0/1000000000) * 100

# Variables and Strings - Variables

speed_of_light = 299792458
billionth = 1.0 / 1000000000
nanostick = speed_of_light * billionth * 100
print nanostick

# Variables and Strings - Variables Quiz

# Given the variables defined here, write Python 
# code that prints out the distance, in meters, 
# that light travels in one processor cycle. 

speed_of_light = 299792458.0 # meters per second
cycles_per_second = 2700000000.0 # 2.7GHz processor

print speed_of_light / cycles_per_second

cycle_distance = speed_of_light / cycles_per_second
print cycle_distance
print cycle_distance * 100 # convert to centimeters

# Variables and Strings - Varying Variables Quiz 1

hours = 9
hours = hours + 1
hours = hours * 2

print hours

# Variables and Strings - Spirit Age Quiz

# Write Python code that defines the vaiable age to be your age in years,
# and then prints out the number of days you have been alive.

age = 46
days_in_year = 365.25 # to account for a leap year every 4 years
print age * days_in_year