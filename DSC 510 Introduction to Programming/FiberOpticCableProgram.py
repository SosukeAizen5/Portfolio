# Fiber Optic Cable Cost Program
# DSC 510
# Week 2
# Programming Assignment Week 2
# David Berberena
# 9/10/2023

# Program Start

# Ask the user for their name
username = input("Please tell us your name.\n")
# Greet the user by confirming the program has received the user's name
print(f'Hello, {username}! Thank you for choosing this program to meet your cable installation cost needs.\n')
# Proceed by asking the user for their employer company name
company = input('Please tell us the name of the company that you work for.\n')
# Thank the user for telling the program the company name
print(f"Thank you for letting us know that you work for {company}! Let's work on your installation costs next.\n")
# Ask the user how many feet of cable will they need to complete the installation process
feet = (input('How many feet of cable (numeric answer only) will you require to complete your installation?\n'))
print(float(feet))
# Confirm the user's input by repeating it back to them
print(f"You have listed the number {feet} as the feet needed to complete your installation. Great, let's continue.\n")
# Alert the user that the cost of the cable is $0.87 per foot.
cost = 0.87
print(f"{company} has determined that each foot of cable costs ${cost}. I can now calculate the total cost for you.\n")
# Calculate total cost of cable
total = cost * feet
print(f"The total cost of your fiber optic cable installation is ${total}. I hope that this answers your cost needs!\n")
# Alert the user that a receipt will be generated for their records.
print("A receipt of this information will be generated for your records.\n")
# Notification of receipt generation
print("Your receipt is listed here:\n")
# Receipt is printed with all necessary information
print("Fiber Optic Cable Program Receipt\n")
print(f"Company name: {company}")
print(f"Company employee: {username}")
print(f"Number of feet of fiber optic cable to be installed: {feet}")
print(f"Total cost of cable installation: ${total}\n")

print('Thank you for using this program, please back come soon!\n')
