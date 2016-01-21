# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input.

# A list of replacement words to be passed in to the play_game procedure.
parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN", "NAME",
                    "VERB", "OCCUPATION", "ADJECTIVE"]

# The following are some test strings to pass in to the play_game procedure.
test_string1 = """Hi, my name is NAME and I really like to VERB PLURALNOUN. I'm also a OCCUPATION at PLACE."""
test_string2 = """PERSON! What is PERSON going to do with all these ADJECTIVE PLURALNOUN? Only a registered OCCUPATION could VERB them."""
test_string3 = """What a ADJECTIVE day! I can VERB the day off from being a OCCUPATION and go VERB at PLACE."""

# Checks if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos(word, parts_of_speech):
    """Returns a word if it is a substring included in the list of strings,
    parts_of_speech, else return None"""

    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# Plays a full game of mad_libs. A player is prompted to replace words in
# ml_string, which appear in parts_of_speech, with their own words.
def play_game(ml_string, parts_of_speech):
    replaced = []
    # your code here

    string_of_words = ml_string.split() # split ml_string into list of words

    for word in string_of_words:
        result = word_in_pos(word, parts_of_speech)

        if result != None:
            user_input = raw_input("Enter a " + result + ": ")
            word = word.replace(result, user_input) # This will keep punctuation
            replaced.append(word)
        else:
            replaced.append(word)

    final_string = " ".join(replaced) # join the list of words back to a string
    return final_string

print play_game(test_string1, parts_of_speech)
# print play_game(test_string2, parts_of_speech)
# print play_game(test_string3, parts_of_speech)
