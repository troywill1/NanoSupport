# Decisions and Repitition: Equality Comparisons

print 2 < 3
print 21 < 3
print 7 * 3 < 21

print 7 * 3 != 21
print 7 * 3 == 21 # '=' means assignment, '==' mean equality

# Decisions and Repitition: Decision Making Playground

print "Example 1: Greater-than and less-than comparisons"
print 2 > 1
print 1 > 2
print 5 < 20
print 100 < 19

print "Example 2: Equality and non-equality comparisons"
print 5 == 5
print "hello" == "hello"
print 5 == 10
print 5 == '5' # What do you think will happen here?
print 7 != 10
print 7 != 7

print "Example 3: A demo of what you are about to learn"
if 3 < 5:
	print "Three is definitely smaller than 5!"

if 10 > 20:
	print "Did you know that 10 is greater than 20!?"
else:
	print "20 is greater than 10"

# Decisions and Repitition: If Statements

def absolute(x):
	if x < 0:
		x = -x
	return x

print absolute(10)
print absolute(-10)

# Define a procedure, bigger, that takes in two numbers
# as inputs, and returns the greater of the two inputs.

def bigger(x,y):
	if x > y:
		return x
	else:
		return y

print bigger(2,7)
print bigger(3,2)
print bigger(3,3)

# Decisions and Repitition: Is Friend

# Define a procedure, is_friend, that takes a string as
# its input, and returns a Boolean indicating  if the 
# input string is the name of a friend. Assume I am friends
# with everyone whose name starts with 'D' and no one else.
# You do not need to check for the lowercase 'd'.

def is_friend(friend):
	if friend[0] == 'D':
		return True # Boolean value, not string
	else:
		return False # Boolean value, not string

print is_friend('Diane')
print is_friend('Fred')

# Or, an easier way:

def is_friend2(name):
	return name[0] == 'D' # The result of this evaluation is a Boolean

print is_friend2('Diane')
print is_friend2('Fred')