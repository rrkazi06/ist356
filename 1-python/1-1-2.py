# Code Challenge 1-1-2
# Let’ write a program to divide up the check among diners in a party.

# Write a program to input the amount of a restaurant check, tip %, and number of diners
check_amount = float(input("Enter the total amount of the bill $"))
if check_amount < 0:
	print("The check amount can't be negative.")
	exit()

tip_percent = int(input("What % would you like to tip, eg. 20 == 20%? "))
if tip_percent < 0:
	print("The tip percentage can't be negative.")
	exit()

number_of_diners = int(input("How many diners? "))
if number_of_diners <= 0:
	print("The number of diners must be greater than zero.")
	exit()

# The program should output the total amount with tip, and the amount each diner owes.
total_amount = check_amount + check_amount * tip_percent / 100
amount_per_diner = total_amount / number_of_diners
print("Total Bill, with Tip:", total_amount)
print(f"Even share among {number_of_diners} diners is {amount_per_diner:.2f}")
# you want to develop the skill of prompting the AI to get the right output on the first try by being specific and clear with what you want it to say
