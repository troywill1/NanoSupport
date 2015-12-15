# Write code for the function random_noun, which takes in no inputs but outputs
# one of two nouns randomly. Use the randint function to generate a number
# from 0-1 and return a noun depending on whether the number is equal to 0 or 1.
# Feel free to experiment with different nouns, but for submission purposes
# return the string "sofa" if the number is 0, else return "llama".

from random import randint # This is new, will learn more about it later

def random_noun():

    noun = randint(0,1)

    if noun == 0:
        return 'sofa'
    else:
        return 'llama'

print random_noun()

# Write code for the function random_verb, which takes in no inputs but outputs
# one of two verbs randomly. Use the randint function to generate a number
# from 0-1 and return a verb depending on whether the number is equal to 0 or 1.
# Feel free to experiment with different verbs, but for submission purposes
# return the string "run" if the number is 0, else return "kayak".

def random_verb():

    verb = randint(0,1)

    if verb == 0:
        return 'run'
    else:
        return 'kayak'

print random_verb()

# Write code for the function word_transformer, which takes in a string word
# as input. If the word is equal to "NOUN", return a random noun, if word is
# equal to "VERB", return a random verb, else return the first character of word

def word_transformer(word):

    if word == 'NOUN':
        return random_noun()
    if word == 'VERB':
        return random_verb()
    else:
        return word[0]

print word_transformer('NOUN')
print word_transformer('VERB')
print word_transformer('bunk')
