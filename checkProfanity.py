# Lesson 3.3c: Use Classes
# Mini-Project: Check Profanity

# Typos can be embarrassing! Imagine how you'd feel if you accidentally
# sent your boss an email that said "I'll take a sh!t at it" instead of "I'll
# take a shot at it". Write a program that can detect curse words in a
# string of text.

# Use this space to describe your approach to the problem.
#
# 1. Read text sample
# 2. Compare against known curse words
# 3. Return result

import urllib

def read_text():
    # Your code here
    quotes = open("/Users/troy/Dropbox/MOOC/ProgNano/Python/movie_quotes.txt")
    contents_of_file = quotes.read()
    # print contents_of_file
    quotes.close()

    check_profanity(contents_of_file)

def check_profanity(text):
    # Your code here
    connection = urllib.urlopen("http://www.purgomalum.com/service/containsprofanity?text=" + text)
    output = connection.read()
    print output
    connection.close()

    if "true" in output:
        print "Profanity Alert!!"
    elif "false" in output:
        print "This document has no profanity."
    else:
        print "Could not scan the document properly."

read_text()
