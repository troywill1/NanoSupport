# Variables and Strings - Strings

print 'Hello'
print "Hello"
hello = "Howdy"
print hello

# Variables and Strings - Hello!!!

name = "Troy Williams"
print name
print "Hello " + name # '+' means concatenation when used with strings

# print "Hello" + 9 - This would return a syntax error

print "!" * 12 # This repeats the string 12 times

print 4
print "4"
print 4 + 4
print "4" + "4"

# Some easy mistakes to mistakes
# print 'hello"
# print hello
# print "hello

# Variables and Strings - Indexing Strings

name = "Troy"
print name[0]
print name[1]
print name[2]
print name[3]

print name[-1] # negative numbers start at the end of the string
print name[-2]

# Variables and Strings - Selecting Sub-Sequences

word = 'assume'
print word[3]
print word[3:4]
print word[4:6]	# print from position 4 to 5
print word[4:]	# print from position 4 to the end
print word[:2]	# print from the beginning to position 1
print word[:]	# print from the beginning to the end

# Stage 2: Work Session 2 - Strings and Variables Demo 1

# Are you wondering why there's two ways to make strings
# (single quotes AND double quotes)??

# Look at the code below. How would we have written that
# if the only Python string character were the double quote?

div_with_class = '<div class="concept-description">'
just_the_class = div_with_class[5:-1]
print just_the_class

# Stage 2: Work Session 2 - Strings and Variables Practice 2

# In addition to using singel quotes (') or double quotes (")
# to create a string, you can also use TRIPLE quotes to create
# a multi-line string.

print """I am a string
that takes up
multiple lines"""

print '''I am also a string
that takes up multiple lines!'''

print '''
<div class="concept">
	<div class="concept-title">
		Multi-line strings
	</div>
	<div class="concept-description">
		Multi-line strings can be made with triple single
		quotes or triple double quotes. But I'm not sure
		why they are useful yet.
	</div>
</div>
'''

# Stage 2: Work Session 2 - Strings and Variables Practice

# Use string sequence to take the single HTML <div> element
# below (written on one line) and then prints it up as three lines.

# The first line should just be the opening tag: <div>
# The second line should be the text within the div (don't forget to indent)
# The third line should just be the closing tag: </div>

div_element = "<div>I am learning to code!</div>"

opening_tag = div_element[:5]	# add the appropriate numbers to each side of the colon
indent = '    '					# modify this string so that it indents the inner text
inner_text = div_element[5:-6]	# add the appropriate numbers to each side of the colon
closing_tag = div_element[-6:]	# add the appropriate numbers to each side of the colon

print opening_tag
print indent + inner_text
print closing_tag

# This is a better solution because it is general and will work no matter what the 
# text between the <div> tags.
