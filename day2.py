#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Create greeting
print("Welcome to Jhayda's tip calculator.")
# Ask for the bill
bill = float(input("What was the total bill? $"))
# Ask for the tip
tip = int(input("What percentage tip would you like to give? 10, 12, or 15 (Please don't add percent sign)? "))
# Ask for the number of people
people = int(input("How many people to split the bill?"))
# Calculate the tip
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
# Calculate the bill per person
bill_per_person = total_bill / people
# Round the bill per person to 2 decimal places
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
# Print the final amount
print(f"Each person should pay: ${final_amount}")