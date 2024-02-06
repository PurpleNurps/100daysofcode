# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

# IN JAVASCRIPT
# if (number % 2 === 0) {
#   console.log("This is an even number.")
#   else {
#   console.
  
  print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120 :
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age < 12 :
    print ("Please pay $5.")
  elif age >= 18 :
    print ("Please pay $12.")
  elif age < 18 :
    print ("Please pay $7.")
else :
  print ("Sorry you are a too short.")

# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height ** 2

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

    # Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  print("Leap year")
else:
  print("Not leap year")

# Which year do you want to check?
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")