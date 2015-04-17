import sys #importing the sys module
from random import choice #from the random module import choice class

def make_chains(corpus): #calls the function "make_chains" with the argument "corpus"
    """Takes input text as string; returns dictionary of markov chains."""

    markov_dict = {} #create an empty dictionary called markov_dict

    terms_list = corpus.split() #taking the argument corpus and spliting it into a list

    for item in range(len(terms_list) - 2): #iterate every item in the range of the list which includes the last index (-2)
        key = (terms_list[item], terms_list[item + 1]) #the key is equal to a tuple of item, item + 1 from the terms_list
        value = terms_list[item + 2] #the value is equal to the list of item + 2

        if key not in markov_dict: #if the key(tuple) is not in the dictionary 
            markov_dict[key] = [] #then add the key to the dictionary

        markov_dict[key].append(value) #adding to the dictionary the key and appending the value (tying it all together)

    return markov_dict #returns the dictionary that we just created!


def make_text(chains): #calls the function "make_text" with the argument chains
    """Takes dictionary of markov chains; returns random text."""

    key = choice(markov_dict.keys())
    terms_list = [key[0], key[1]]

    while key in markov_dict:
        # Keep looping until we have a key that isn't in the chains
        # (which would mean it was the end of our original text)
        #
        # Note that for long texts (like a full book), this might mean
        # it would run for a very long time.

        word = choice(markov_dict[key])
        terms_list.append(word)
        key = (key[1], word)

    return " ".join(terms_list)

input_path = sys.argv[1]
input_text = open(input_path).read()

# Get a Markov chain
markov_dict = make_chains(input_text)

# Produce random text
random_text = make_text(markov_dict)

print random_text
