# Stage 1: Make your Web Page

# Webpages, Documents & Structure

## The Basics of the Web & HTML

HTML (HyperText Markup Language) is the backbone of the web.

A web page is a text document written in a language called HTML. Web browsers read these documents, and then interpret and display them.

*Tag*: An HTML tag is always contained within angled brackets. Most tags have an opening tag and a closing tag. Some tags (called "void" tags) do not require a closing tag.

*Element*: An HTML element refers to everything within a set of opening and closing tags.

*Attribute*: This is a property of an HTML element.

### HTML Tags

```html
<TAG>contents</TAG>
```

* **Bold**

```html
<b>contents</b>
```

* *Emphasis (Italiac)*

```html
<em>contents</em>
```

### HTML Attributes

```html
<TAG ATTR="value">contents</TAG>
```

* Anchor (links)

```html
<a href="www.reddit.com">derp</a>
```

* Image (void tag; has no content, so it doesn't need a closing tag)

```html
<img src="url" alt="text">
```

* Break (void tag; inline - just creates a line break)

```html
<br>
```

* Paragraph (block - creates an invisible block around the text that has height and weight)

```html
<p>contents</p>
```

* Span (inline - container for text that can contain a CSS class)

```html
<span class="foo">contents</span>
```

* Div (block - a container that can contain a CSS class)

```html
<div class="bar">contents</div>
```

## Creating a Structured Document with HTML

* HTML and CSS are both "languages"
* HTML controls the "structure" of a web page
* CSS controls the "style" of a page (how it looks).
* When programmers talk about the "DOM" (Document Object Model) they are talking about the tree-like structure of a page.

* To learn more about what a "tree-like structure" means, read the first two paragraphs of the wikipedia article on [Tree Structures](http://en.wikipedia.org/wiki/Tree_structure).

* Everything on a webpage is a box. Use <div> to define a block of content, or create "boxes", to give structure to a document with HTML.

* Use "Developer's Tools" in Google Chrome to view the structure of a webpage.

## Adding CSS Style to HTML Structure

What is CSS?

* CSS (Cascading Style Sheets) is code that controls the "style" of HTML elements

How does CSS control HTML?

* Let's say you want all "h1" elements to have a black background and white text:

```css
h1 {
  background-color: black;
  color: white;
}
```
* "h1" is a _selector_
* Everything between the curly braces is a _rule_
* "background-color" is an _attribute_
* "black" is a _value_

* If you only want to add style to certain "h1" elements, you can use _class selectors_:

```html
<div class="stop"></div>
<div class="slow"></div>
<div class="go"></div>

<style>
  div {
    height : 50px;
    width : 50px;
    border-radius: 25px;
  }
  .stop {
    background-color: red;
  }
  .slow {
    background-color: yellow;
  }
  .go {
    background-color: green;
  }
</style>
```

* In the "style" HTML element, you refer to the class with ".class-name"
* Notice how styles can be added to all "div"s or just certain "div"s using the appropriate selector.

How do I include CSS styling in my web page?

* Method 1: Write CSS in the &lt;head&gt; element of the HTML document. This method is good for very small projects:

```html
<head>
  <style>
    div {
      background-color : red;
    }
  </style>
</head>
<body>
  <div>
    This will have a red background.
  </div>
</body>
```

* Method 2: Link your HTML to a separate CSS file. This lets you stay more organized when working on larger projects. For example, you could have a file named "main.html":

```html
<head>
   <link rel="stylesheet" type="text/css" href="main.css">
</head>
<body>
  <div>
    This will have a red background.
  </div>
</body>
```

and in the same folder you could have a file named "main.css":

```css
div {
  background-color : red;
}
```
* Method 3: Write style "inline" with HTML. This is a bad idea because it leads to lots of repeated code and is hard to read. With this method, you modify the style attributes of _every_ HTML element:

```html
<body>
  <div style="background-color: red; color: white">
    This div will have a red background and white text.
  </div>
  <div style="background-color: red; color: white">
    So will this one.
  </div>
  <div style="background-color: red; color: white">
    Now, what if I change my mind?
  </div>
  <div style="background-color: red; color: white">
    I'd rather have a black background...
  </div>
  <div style="background-color: red; color: white">
    Never do this!
  </div>
</body>
```

# Stage 2: Automate Your Page

# Telling Computers What To Do

## Introduction to "Serious" Programming

* _Computer_ - A universal machine that is useless unless it is given some sort of program, or set of instructions, to execute. Given a program, a computer can become many different things.

Why do we need to invent languages like Python to program computers instead of using natural languages like English?

* _Ambiguity_ - natural languages are ambiguous, but we need the computer to execute the code the exact way that the programming intended.

* _Verbosity_ - natural languages are verbose; we need to describe exactly what the computer needs to do in a very precise sequence of steps.

### Backus-Naur Form

* A way to describe a computer language: <Non-terminal> -> replacement
* John Backus was the lead designer of FORTRAN at IBM (1950s)

```
Sentence	-> Subject Verb Object
Subject		-> Noun
Object		-> Noun
Verb		-> Eat
Verb		-> Like
Noun		-> I
Noun		-> Python
Noun		-> Cookies
```

"Python Eat Cookies" and "Python Eat Python" both follow the "Subject Verb Object" grammar.
"I Like Eat" does not.

```
Expression -> Expression Operator Expression
Expression -> Number
Operator -> +
Operator -> *
Number -> 0,1,...
Expression -> (Expression)
```

3, (1*(2*(3 * 4))), (((7))) follow the Expression Operator Expression grammar.
((3), +33 would not follow the grammar.

## Variables and Strings

### Variables

```python
speed_of_light = 299792458
billionth = 1.0 / 1000000000
nanostick = speed_of_light * billionth * 100
print nanostick
```

```python
days = 7 * 7    # the right side is evaluated first
days = days - 1

# "=" means assignment *not* equals; think of it like an arrow.
# days <- days - 1
```

### Strings

```python
name = "Troy Williams"
print name
print "Hello " + name

# '+' means concatenation when used with strings

# print "Hello" + 9 - This would return a syntax error

print "!" * 12 # This repeats the string 12 times
```

#### Indexing Strings

```python
<string> [<expression>]

'udacity'[0] -> 'u'
'udacity'[1 + 1] -> 'a'
```
#### Selecting Sub-Sequences

```python
<string> [<expression>:<expression>]

    s       start       stop

# Evaluates to a string that is a subsequence of the characters in 's',
# starting from position 'start' and ending in position 'stop - 1'

word = 'assume'
print word[3]
print word[3:4]
print word[4:6]	# print from position 4 to 5
print word[4:]	# print from position 4 to the end
print word[:2]	# print from the beginning to position 1
print word[:]	# print from the beginning to the end
```

#### Finding Strings in Strings

```python
<string>.find(<string>)

# The output: number that gives the first position in the
# search string where the target string appears. If the target
# string is not found then -1 is returned.

pythagoras = 'There is geometry in the humming of the strings, there is music in the spacing of the spheres.'

print pythagoras.find('string')
print pythagoras[40:]
print pythagoras.find('T')
print pythagoras.find('sphere')
print pythagoras[86:]
print pythagoras.find('algebra')
```

```python
<string>.find(<string>, <number>)

# The output: number that gives the first position in the
# search string where the target string appears, *after* the position
# passed in as the 2nd parameter (<number>).
# If the target string is not found then -1 is returned.

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
```

## Input -> Function -> Output

### Using Procedures

* A way to map inputs to outputs

```
<procedure>(<input>, <input>,...)
            operands or arguments
```

```python
def rest_of_string(s):
  return s[1:]

print rest_of_string('audacity')
```

On the first line of your function definition...

* You must begin the line with **def** (lowercase)
* After **def** you must give a function name (in this case it will be **rest_of_string**)
* Next, you must have a set of parentheses **with the required parameters inside**
* The line must end with a **:** (colon)

In the body of the function...

* Every line in the function must be indented
* If you want your function to produce output, it must end with a **return** statement

To "call" the function...

1. The function name, followed by...
2. ...an open paren **(**, followed by...
3. ...the values for the required parameters, followed by...
4. ...a closed paren **)**

## Decisions and Repetition: If and While

### Equality Comparisons

```python
# Decisions and Repitition: Equality Comparisons

print 2 < 3
print 21 < 3
print 7 * 3 < 21

print 7 * 3 != 21
print 7 * 3 == 21 # '=' means assignment, '==' mean equality
```

### If Statements

```python
if <Test Expression>:
  <Block> # block will execute 0 or 1 times
<Code>    # will execute regardless of the test expression
```
```python
def absolute(x):
  if x < 0:
    x = -x
  return x

print absolute(10)
print absolute(-10)
```

```python
if <Test Expression>:
  <Block>
else:
  <Block>
```

### Or Operator

```
<Expression> or <Expression>

If the first expression evaluates to True, the value is True
and the second expression is not evaluated.

If the first expression evaluates to False, the value is the
value of the second expression.
```

### Every Possible Computer Program

We now know enough to write, in theory, every possible computer program. All that is needed:

* Arithmetic
* Comparisons
* Procedures
* If Statements

This was proven in the 1930s by Alan Turing (1912-1954):

* Developed abstract model of a computer (1936), "Turing Machine"
* Proved that a machine with a few simple operations could simulate any other machine

### While Loops

```
while <Test Expression>
  <Block> # Will execute 0, 1, 2,...times
```

```
while <Test Expression>
  <Code>
  if <Break Test>
    break
  <More Code>

<After While>
```

## Structured Data: Lists and For Loops

### Lists

* **String** - Sequence of characters

```python
s = 'yabba!'
s[0] -> 'y'
s[2:4] -> 'bb'
```

* **List** - Sequence of _anything_

```python
p = ['y', 'a', 'b', 'b', 'a', '!']
p[0] -> 'y'
p[2:4] -> ['b', 'b']

<list> -> [<expression>, <expression>,...]
```

### For Loops

```python
For <name> in <list>:
  <Block>

def print_all_elements(p):
  for e in p:
    print e
```

### List Index (with in)

```python
def find_element2(list, element):
	if element in list:
		return list.index(element)
	else:
		return -1
```

```python
def find_element3(list, element):
	if element not in list:
		return -1
	else:
		return list.index(element)
```

## Debugging

### Debugging Strategy Recap

* Examine error messages when programs crash
* Work from example code
* Make sure examples work
* Check (print) intermediate results
* Keep and compare old versions

### Commenting Code

1. Don't comment obvious code
2. Start functions with a comment
3. Keep comments up-to-date
4. Be concise

# How to Solve Problems

## Pythonista's Guide to All Problems in the Galaxy

1. Don't Panic!
2. What are the inputs?
3. What are the outputs?
4. Work through some examples by hand
5. Simple mechanical solution:

```
days = 0
  while date1 is before date2:
    date1 = advance to next day
    days += 1
  return days
```

6. Develop incrementally and test as you go

* Don't optimize prematurely!
  * Simple and correct
* Making progress is good!
  * Write small bits of code, test them, know what they do
