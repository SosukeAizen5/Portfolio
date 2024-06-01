# Function definition file for the creation of text file parsing functions

# built-in Python string library must be imported to use string manipulation built-in functions

import string

# add_word function is defined, which will create a dictionary (this dictionary will be a global variable in main)
# where each new word will be stored and the count of each word will be stored using an if/else conditional statement


def add_word(word, word_count):
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1

# process_line function is defined, which will use string manipulation to process each line of the text file
# by ridding the line of all punctuation and spaces, making all words lowercase, and making those words into variables
# The previously defined add_word function is called at the end of this function to fulfill the for loop conditions


def process_line(line, word_count):
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        add_word(word, word_count)

# process_file function is defined to display the results of the last two functions in a readable format for the user
# Spacing is important in a tabular dataset that does not use an actual table,
# so this function is coded accordingly using for loops


def process_file(occurrences):
    longest_term = 1
    length_list = []
    result = ''
    for row in occurrences:
        length = len(str(row[1]))
        length_list.append(length)
        if length > longest_term:
            longest_term = length

# This for loop is important to return the resulting tabular format, as not returning it causes the function to output
# the enumerated words and values as None type, which cannot be manipulated properly

    for term, row in enumerate(occurrences):
        length = length_list[term]
        spacing = (longest_term - length) * ' '
        result += f"{row[1]}{spacing}{row[0]}\n"
    return result
