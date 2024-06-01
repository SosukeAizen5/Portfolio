# Fiber Optic Cable Cost Program (Function Creation and Bulk Discount Applied)
# DSC 510
# Week 4
# Programming Assignment Week 4
# David Berberena
# 9/24/2023

# Program Start
import FirstModule

# Ask the user for their name
username = input("Please tell us your name.\n")
# Greet the user by confirming the program has received the user's name
print(f'Hello, {username}! Thank you for choosing this program to meet your cable installation cost needs.\n')
# Proceed by asking the user for their employer company name
company = input('Please tell us the name of the company that you work for.\n')
# Thank the user for telling the program the company name
print(f"Thank you for letting us know that you work for {company}! Let's work on your installation costs next.\n")
# Ask the user how many feet of cable will they need to complete the installation process
print('How many feet of cable will you require to complete your installation?\n')
while True:
    feet = input('Please enter a number:\n')

    try:
        float_value = float(feet)
    except ValueError:
        print('You have entered an invalid response. Please enter a numerical value only.\n')
    else:
        break
# Confirm the user's input by repeating it back to them
print(f"You have listed {float_value} as the feet needed to complete your installation. Great, let's continue.\n")
# Alert the user that the cost of the cable is a certain amount based on the length of cable required
# $0.87 for cable 100 feet or fewer
# $0.80 for cable 101-250 feet
# $0.70 for cable 251-500 feet
# $0.50 for cable 501 feet or more
if float_value <= 100:
    cost = 0.87
elif 100 < float_value <= 250:
    cost = 0.80
elif 250 < float_value <= 500:
    cost = 0.70
else:
    cost = 0.50
print(f"{company} has determined that each foot of cable costs ${cost}. I can now calculate the total cost for you.\n")


# Calculate total cost of cable
def main():
    print(f"The total cost of your fiber optic cable installation is ${FirstModule.calculate_cost(feet)}.")


if cost == 0.80:
    discount = 0.07
elif cost == 0.70:
    discount = 0.17
elif cost == 0.50:
    discount = 0.37
else:
    discount = 0.00

if __name__ == '__main__':
    main()
print("I hope that this answers your cost needs!\n")
# Alert the user that a receipt will be generated for their records.
print("A receipt of this information will be generated for your records.\n")
# Notification of receipt generation
print("Your receipt is listed here:\n")
# Receipt is printed with all necessary information
print("Fiber Optic Cable Program Receipt\n")
print(f"Company name: {company}")
print(f"Company employee: {username}")
print(f"Number of feet of fiber optic cable to be installed: {feet}")
main()
print(f"You have received a discount of ${discount} per foot based on the number of feet ordered!\n")

print('Thank you for using this program, please back come soon!\n')
