# Temperature Program
# DSC 510
# Week 6
# Programming Assignment Week 6
# David Berberena
# 10/8/2023

# Program Start

# This program will be used to have the user input temperatures into a list so the program can tell the user
# the largest temperature, the smallest temperature, and the number of temperatures that have been input

# Import Temp_Function_File for proper temperature function call to main

import Temp_Function_File

# Call functions to implement program

if __name__ == "__main__":
    Temp_Function_File.program_greeting()
    Temp_Function_File.temperature_function()
    Temp_Function_File.temp_values()
    Temp_Function_File.program_ending()
