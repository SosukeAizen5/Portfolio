# Calculator Program (Calculates +, -, *, /, and average)
# DSC 510
# Week 5
# Programming Assignment Week 5
# David Berberena
# 10/1/2023

# Program Start

# Imported the file with the function definitions to call within the main program

import CalculationsFile

# While loop to allow the program to run until a sentinel value has been input by the user
# Welcome statement for the user to be introduced to the program and its abilities

while True:
    print('Welcome to the Calculator Program! This program can calculate basic mathematical equations such as '
          'addition, subtraction, multiplication, division, and the average of any given list.\n')

# Prompt the user to define which calculation they wish to make
# Conditional statement allows the user to choose the specific function they need to call it to main

    print('Please enter "BasicOps" or "Average" to choose which program you would like to initiate:\n')
    operation = input()
    if operation == 'BasicOps':
        CalculationsFile.perform_calculation()
    elif operation == 'Average':
        CalculationsFile.perform_average_calculation()
    else:
        print('You have entered an unknown program. Please enter one of the two specified programs above.\n')

# While loop question at the end of the program allowing for the loop to restart or a sentinel value to end the program

    user_input = input('Would you like to perform another calculation?\n')
    if user_input not in ['Yes', 'yes', 'YES']:
        print('Thank you for using the Calculator Program! Have a nice day!')
        break
