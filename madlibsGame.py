# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input.

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """Straight outta PLACE, crazy NOUN named PERSON, from the gang called PLURALNOUN Wit Attitude"""

def word_in_pos(word, parts_of_speech):
    """Returns word if it is a substring included in the list of strings,
    parts_of_speech, else return None"""

    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def play_game(ml_string, parts_of_speech):
    replaced = []
    # your code here
    sub_word = "corgi"
    len_sub_word = len(sub_word)

    string_of_words = ml_string.split() # Split ml_string into list of words

    for word in string_of_words:
        result = word_in_pos(word, parts_of_speech)
        if result == None:
            replaced.append(word)
        else:
            for pos_word in parts_of_speech:
                if pos_word == word:
                        replaced.append(sub_word)

            replaced.append(sub_word + word[-1])

    final_string = " ".join(replaced) # Join the list of words back to a string
    return final_string

print play_game(test_string, parts_of_speech)
