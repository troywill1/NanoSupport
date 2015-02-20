# Imagine you wanted to write code that extracted the
# text from an HTML div...

html_div = "<div>This is some text</div>"
div_text = html_div[5:-6]

print div_text

# Can you modify the code below to print out the text
# inside of an HTML <b> element?

html_b = "<b>And this is even more text</b>"
b_text = html_b[3:-4] # Thi is the line you should modify
print b_text

# Variables and Strings - Capital Udacity Quiz

# Write Python code that prints out 'Udacity' (with a capital 'U)',
# given the definition of 's' below.

s = 'audacity'
print "U" + s[2:]

# Variables and Strings - Understanding Selection Quiz

s = 'audacity'
print s[:3] + s[3:]
t = 'Hi'
print t[:3] + t[3:]

# Variables and Strings - Finding Strings in Strings

pythagoras = 'There is geometry in the humming of the strings, there is music in the spacing of the spheres.'

print pythagoras.find('string')
print pythagoras[40:]
print pythagoras.find('T')
print pythagoras.find('sphere')
print pythagoras[86:]
print pythagoras.find('algebra')

# More examples of finding strings within strings

print "Example 1: Finding substrings in a string"
print "test".find('te')
print "test".find('st')
print "test"[2:]

print "Example 2: Finding substrings in a string which is stored as a Variable"
my_string = "test"
print my_string.find('te')
print my_string.find('st')
print my_string[2:]

print "Example 3: Printing out everything after a certain substring"
my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
favorite_color = my_string[color_start_location:]
print favorite_color # Opps, this line prints out 'color: ' as well...
print favorite_color[7:] # This fixes it!

print "Example 4: Other interesting things about string.find()..."
print "text".find("text")	# prints 0
print "text".find("Text")	# prints -1
print "text".find("")		# prints 0
print "text".find(" ")		# prints -1

# Variables and Strings - Finding with Numbers

danton = "De l'audace, encore de l'audace, toujours de l'audace."

print danton.find('audace')
print danton.find('audace', 0)
print danton.find('audace', 5)
print danton.find('audace', 6)
print danton[6:]
print danton[25:]
print danton.find('audace', 25)
print danton.find('audace', 26)
print danton[47:]
print danton.find('audace', 48)

# More examples of finding strings with numbers

print "Example 1: Using find to print the second occurrence of a sub-string"
print "test".find('t')
print "test".find('t', 1)

print "Example 2: Using a variable to store first location"
first_location = "test".find('t') # here we store the first location of "t"
print "test".find('t', first_location + 1) # then use that location to find the 2nd occurrence

print "Example 3: Using find to get rid of exclamation marks!!"
example = "Wow! Python is great! Don't you think?"
first = example.find('!')
second = example.find('!', first + 1)
new_string = example[:first] + example[first + 1:second] + example[second + 1:]
print new_string # Opps, I should probably replace the !s with periods
new_string = example[:first] + '.' + example[first + 1:second] + '.' + example[second + 1:]
print new_string
