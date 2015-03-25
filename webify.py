# Stage 2: Work Session 4 -> Step 4: Write new Code (part 1)

def get_title(titleString):

	title_location = titleString.find('TITLE:') # here we store the location of "TITLE:"
	description_location = titleString.find('DESCRIPTION:') # find the 'DESCRIPTION:' location

	return titleString[title_location + 7 : description_location]

def get_description(descriptionString):

	description_location = descriptionString.find('DESCRIPTION:') # find the 'DESCRIPTION:' location

	return descriptionString[description_location + 13 :]

# Stage 2: Work Session 4 -> Step 4: Write new Code (part 2)

# Now you'll write the 'get_concept_by_number' function. It will take 2 inputs. The first
# will be text (like in the EXAMPLE_TEXT) shown below. The second will be a number.
# If that number is 1, the function should return the FIRST concept. If it's 2, the second...
# This is a HARD problem. Give it a shot, but don't worry if you don't get it.
# You'll see the solution next.

def get_concept_by_number(text, concept_number):

	while concept_number >= 1:

		title_location = text.find('TITLE:') # find the location of 'TITLE:''
		description_location = text.find('DESCRIPTION:') # find the 'DESCRIPTION:' location
		next_title = text.find('TITLE:', description_location + 1) # find the next 'TITLE:'

		parsedText = text[title_location : description_location] + text[description_location : next_title]

		text = text[next_title:]

		concept_number = concept_number - 1

	return parsedText

# Procedure from prior work session that will be used in this project.
# Also included in the file 'procedures.py'.

# Stage 2: Work Session 3 - Automatically Generate HTML

# Write a function that takes a concept title and a concept
# description as input and then returns HTML that you can copy
# and paste into your notes web page.

def webify(conceptTitle, conceptDescription):
	return '''
	<div class="concept">
		<div class="concept-title">
			''' + conceptTitle + '''
		</div>

		<div class="concept-description">
			''' + conceptDescription + '''
		</div>
	</div>'''

#print webify('Troy Title', 'Troy Description')

# Stage 2: Work Session 4 -> What we have so far

# That's all we'll do for now. But if you're feeling ambitious,
# try writing a 'generate_all_html' function that automatically
# makes the HTML for all the concepts in the text.

def generate_all_html(inputText):

	conceptNumber = 1
	concept = get_concept_by_number(inputText, conceptNumber)
	all_html = ''

	while concept != '':
		title = get_title(concept)
		description = get_description(concept)
		concept_html = webify(title, description)
		all_html = all_html + concept_html
		conceptNumber = conceptNumber + 1
		concept = get_concept_by_number(inputText, conceptNumber)

	return all_html


#concept = '''TITLE: While Loops
#DESCRIPTION: A while loop repeatedly executes the body of the loop until the "test condition" is
#no longer true.'''

#print get_title(concept)
#print get_description(concept)

EXAMPLE_TEXT = '''TITLE: Why Computers are Stupid
DESCRIPTION: The phrase "computers are stupid" refers to how they interpret instructions literally.
This means that small typos can cause big problems.
TITLE: Python
DESCRIPTION: Python is a "programming language." It provides programmers a way to write instructions
for a computer to execute in a wy that the computer can understand.
TITLE: While Loops
DESCRIPTION: A while loop repeatedly excutes the body of the loop until the "test condition" is
no longer true.'''

#print get_concept_by_number(EXAMPLE_TEXT, 2)

print generate_all_html(EXAMPLE_TEXT)