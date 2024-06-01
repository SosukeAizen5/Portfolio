# Gettysburg.txt File Parsing Program Part 2 (New Text File Creation)
# DSC 510
# Week 9
# Programming Assignment Week 9
# David Berberena
# 10/29/2023

# Program Start

# Import the Gettysburg_Functions file to access the three functions
# needed in our main function: add_word, process_line, and process_file

import Gettysburg_Functions_Part_2

# Define word_count as a global variable, which will be the dictionary needed for the imported functions to run

word_count = dict()

# Create a while loop to welcome the user and request the correct file be input for parsing

while True:
    print('Welcome to the Gettysburg Address Parsing Program! If you know the name of the file needed '
          'to use this program, please enter it below.\n')
    correct_file = input()
    # Conditional statement has been coded here to prevent erroneous file names from being entered
    # Once the proper file name is entered, open the Gettysburg.txt file and begin the text parsing by using a
    # for loop which calls process_line, which then also calls add_word
    if correct_file == 'gettysburg.txt':
        with open(correct_file, 'r') as gba_file:
            for line in gba_file:
                Gettysburg_Functions_Part_2.process_line(line, word_count)
        break
    # Error handling statement that ends the program should the wrong file name be entered
    else:
        print('Sorry! The file you entered is not compatible with this program.')
        break

# Establish total_words as a global variable to store the total number of words in the text file

total_words = sum(word_count.values())

# Block of code to change the word count gleaned from process_line to a list that is appended and sorted via a for loop

occurrences = list()
for key, val in list(word_count.items()):
    occurrences.append((val, key))
    occurrences.sort(reverse=True)

# Print statements are written to the new file, regardless of whether the file was correct or not in the above code

with open('new_gba_file.txt', 'w') as new_gba:
    new_gba.write(f'The total number of words in the file is: {total_words}\n')
    new_gba.write('WORD       COUNT\n')
    new_gba.write('________________\n')

# Process_file function is called via a variable amendment to the already written new_gba_file.txt file

tabular_list = Gettysburg_Functions_Part_2.process_file(occurrences)
with open('new_gba_file.txt', 'a') as new_gba:
    new_gba.write(tabular_list)
