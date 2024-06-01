# Cat Fact API Program
# DSC 510
# Week 10
# Programming Assignment Week 10
# David Berberena
# 11/5/2023

# Program Start

# Importing the requests library is necessary for Python to connect with the webpage via the API

import requests

# Define function that holds the API request information and incorporates a conditional statement
# which handles the error potential for a bad server connection


def random_cat_fact():
    api_access = requests.get("https://catfact.ninja/fact")
    if api_access.status_code == 200:
        cat_fact = api_access.json()['fact']
        print('Finding random cat fact for you....\n')
        print(f'{cat_fact}\n')
    else:
        print("Uh-oh! Failed to connect with the cat elders!\n")

# The program can now be written with the definition of random_cat_fact() to call into main

# Welcome statement for the user


print('Welcome to the Random Cat Fact Program, the program for avid cat enthusiasts!\n')

# While loop creation allows for the user to continue gathering more cat facts until they say "no"
# User input is made lowercase to handle any awkward user input such as "YeS, YES, Yes, yES, etc.

while True:
    request = input("Do you want to know a cat fact? Please enter 'yes' or 'no'.\n").lower()

# Conditional statement is needed to print

    if request == "yes":
        random_cat_fact()
    elif request == "no":
        print("Hopefully your cat knowledge has been expanded. We look forward to giving you more facts another time!")
        break
    else:
        print("Didn't quite get that. The cat elders only accept 'yes' or 'no'.\n")
