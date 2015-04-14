import sys


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    green_eggs = open("green-eggs.txt")
    green_eggs_read = green_eggs.read()
    green_eggs_split = green_eggs_read.rstrip().split()
    
    green_eggs_dict = {}

    for words in green_eggs_split:
        

    #for line in green_eggs:
     #   split_line = line.strip().split()
      #  print split_line
   # return {}


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

print sys.argv
# args = sys.argv
# print args

input_text = "Some text"

# Get a Markov chain
chain_dict = make_chains(input_text)

# Produce random text
random_text = make_text(chain_dict)

print random_text
