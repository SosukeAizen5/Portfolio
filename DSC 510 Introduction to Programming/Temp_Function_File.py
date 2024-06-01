# Define function to greet the user

def program_greeting():
    # Ask user for their name

    username = input("Welcome to the Temperature Program! Please tell us your name.\n")

    # Greet the user by confirming the program has received the user's name

    print(f'Hello, {username}! Thank you for choosing our Temperature Program to list the temperatures '
          f'you are working with.\n')


# Establish "temperatures" as a global variable to use in multiple functions

temperatures = []


# Define function to have the user input temperatures into a list when prompted

def temperature_function():
    # Having the user input the list of temperatures requires error handling for entering more than one term at once

    while True:
        temp_input = input('Please list all temperatures (one numerical value at a time) that need to be documented, '
                           'and enter "x" to end your list.\n')

        # Error handling block of code is needed to prevent program from crashing when no temperatures are input

        if temp_input.lower() == 'x':
            if not temperatures:
                print('The program cannot provide any feedback if there are no listed temperatures!')
                continue
            else:
                break

        # While loop continues with the appending of the input values to the empty list
        # Error handling statement is needed for incorrect or non-numerical temperature input

        try:
            temp = float(temp_input)
            temperatures.append(temp)
        except ValueError:
            print('You have entered an invalid temperature. Please try again by inputting a numerical value.')

    # Print statement is needed to show user that the program has computed and stored the user input

    print(f"You have listed these temperatures: {temperatures}\n")

    # Define function that analyzes the temperature list


def temp_values():
    # Use len() to find the number of terms listed

    print(f'The total number of temperatures in your list is: {len(temperatures)}\n')

    # Use max() and min() to find smallest and largest temperature in user's list

    print(f'The smallest temperature you have entered is: {min(temperatures)}\n')
    print(f'The largest temperature you have entered is: {max(temperatures)}\n')


def program_ending():
    # Alert the user that the program has ended

    print('I hope this information has been helpful for your temperature needs.\n')
    print('Thank you for using our program! Enjoy the rest of your day!')
