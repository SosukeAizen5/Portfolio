# Calculator Program (Calculates +, -, *, /, and average)
# DSC 510
# Week 5
# Programming Assignment Week 5
# David Berberena
# 10/1/2023

# Program Start

# Define the Basic Operations ( +, -, *, / ) function
def perform_calculation():
    operation = str(input("Please type the operation that you would like to perform (+ for Addition, - for Subtraction,"
                          " * for Multiplication, / for Division):\n"))

    while True:
        x = input('Enter first number:\n')

# Error handling statements input for potential string inputs for both numbers

        try:
            number1 = float(x)
        except ValueError:
            print('You have entered an invalid response. Please enter a numerical value only.\n')
        else:
            break
    while True:
        y = input('Enter second number:\n')

        try:
            number2 = float(y)
        except ValueError:
            print('You have entered an invalid response. Please enter a numerical value only.\n')
        else:
            break

# Operation calculations are coded and formatted to match the numbers provided by the user and answers are displayed

    if operation == "+":
        print('You have chosen to add {} and {}, which equals:\n' .format(number1, number2))
        print(number1 + number2)

    elif operation == "-":
        print('You have chosen to subtract {} and {}, which equals:\n' .format(number1, number2))
        print(number1 - number2)

    elif operation == "*":
        print('You have chosen to multiply {} and {}, which equals:\n' .format(number1, number2))
        print(number1 * number2)

    elif operation == "/":
        print('You have chosen to divide {} and {}, which equals:\n' .format(number1, number2))

# Additional error handling statement to prevent a Zero Division Error, sending them to the finaL while loop question

        try:
            print(number1 / number2)
        except ZeroDivisionError:
            print('Error: Cannot divide by 0.')

# Statement has been made to alert the user that they have not specified a calculable operation and must restart

    else:
        print('You have entered an invalid operation. Please rerun the program and try again. '
              'Sorry for the inconvenience!')

# Define the Average function


def perform_average_calculation():
    list_num = []

# Having the user input the list of terms requires error handling for entering more than one term at once

    while True:
        number_input = input('Please list all numbers (one term at a time) needed to find your desired average,'
                             ' and enter "x" to end your list.\n')
        if number_input == 'x':
            break
        try:
            term_value = float(number_input)
        except ValueError:
            print('You have entered an invalid term. Please try again.')
        else:
            list_num.append(float(number_input))
    print(f"You have listed these numbers: {list_num}\n")

# For loop to determine len(list_num)

    length_list = 0
    for _ in list_num:
        length_list = length_list + 1
    print(f"The total number of terms in your list is: {length_list}\n")

# For loop to determine sum(list_num)

    sum_list = 0
    for term in list_num:
        sum_list = sum_list + term
    print(f"The total sum of terms in your list is: {sum_list}\n")

# Equation for average and display of final answer

    avg = sum_list / length_list
    print(f"The average of the terms in your list is: {avg}")
