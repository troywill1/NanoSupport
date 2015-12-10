# Section 2.5 Debugging Notes and Code

# A small change will fix the crashing bug in printInches.
 
def printExample(a, b):
    print a + b
   
def printInches(n):
    print str(n) + " inches" # print n + " inches"
 
# Don't change the function calls on lines 10 - 12.
printExample(17, 23)
printExample('long', 'word')
printInches(42)


# When I wrote boldwrap, I didn't copy the functionality of the
# bracket function carefully.  Review my code and catch the mistake.
 
def bracket(text):
    return '[' + text + ']'
 
# def boldwrap(text)
def boldwrap(text):
    return '<b>' + text + '</b>'
 
print boldwrap('This is an important message.')


# Try adding print statements to look at the values of variables inside
# the remove function.  See if you can find out what's making it give
# silly answers such as remove('ding', 'do') -> 'dining'.
 
def remove(somestring, sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub)

    if location == -1: # Added this 'if' statement to fix
    	return somestring
    print location # Added print statement to look at the variables
    length = len(sub)
    print length # Added print statement to look at the variables
    part_before = somestring[:location]
    print part_before # Added print statement to look at the variables
    part_after = somestring[location + length:]
    print part_after # Added print statement to look at the variables
    return part_before + part_after
    
 
#
# Don't change these test cases!
print remove('audacity', 'a')
print remove('pythonic', 'ic')
print remove('substring institution', 'string in')
print remove('ding', 'do')  # "do" isn't in "ding"; should print "ding"
print remove('doomy', 'dooming')  # and this should print "doomy"