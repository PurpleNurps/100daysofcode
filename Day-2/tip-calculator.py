#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
#Welcome to the tip calculator.
print("Welcome to the tip calculator.")
#What was the total bill? 
bill = input("What was the total bill?\n£")
bill = float(bill)
#What percentage tip would you like to give? 10, 12, or 15? 
tip = input("What percentage tip would you like to give? 10, 12 or 15?\n")
tip = float(tip)
tip = tip/100 + 1
#How many people to split the bill? 
people = input("How many people to split the bill?\n")
people = float(people)

#Each person should pay: 
print(f"Each person should pay £{round(bill * tip / people, 2):.2f}")