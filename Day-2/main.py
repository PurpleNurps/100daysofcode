two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
print(int(two_digit_number[0]) + int(two_digit_number[1]))
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
#convert height and weight to float
#square the height
#convert answer to an int
height = float(height)
weight = int(weight)
height = height**2
print(int(weight/height))

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
time_left = 90 - int(age)
weeks_left = time_left * 52
#use an f string to convert and cocatonate the string and int
print(f"You have {weeks_left} weeks left.")