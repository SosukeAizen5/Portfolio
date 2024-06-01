# Gettysburg.txt File Parsing Program
# DSC 510
# Week 8
# Programming Assignment Week 8
# David Berberena
# 10/22/2023

# Program Start

# Import the Gettysburg_Functions file to access the three functions
# needed in our main function: add_word, process_line, and pretty_print

import Gettysburg_Functions

# Define word_count as a global variable, which will be the dictionary needed for the imported functions to run

word_count = dict()

# Open the Gettysburg.txt file and begin the text parsing by using a
# for loop which calls process_line, which then also calls add_word

with open('gettysburg.txt', 'r') as gba_file:
    for line in gba_file:
        Gettysburg_Functions.process_line(line, word_count)

# Establish total_words as a global variable to store the total number of words in the text file

total_words = len(word_count)

# A print statement is created to alert the user to the total number of words (using an f string)
# Additional print statements are generated to categorize the data parsed from the text file

print(f'The total number of words in the file is: {total_words}\n')
print('WORD       COUNT')
print('________________')

# The data gleaned from the parsing functions is a dictionary,
# so this block of code is to turn the dictionary data
# into a list and sort the data into a presentable format

occurrences = list()
for key, val in list(word_count.items()):
    occurrences.append((val, key))
    occurrences.sort(reverse=True)

# pretty_print is called to display the parsed data in a tabular format

Gettysburg_Functions.pretty_print(occurrences)
