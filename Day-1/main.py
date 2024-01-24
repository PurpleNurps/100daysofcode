# Provide any name in the input pane below.
# That value can be accessed using the input() function.
# Don't put anything inside the input() function!
print("Hello" + " Angela")
print("Hello, " + input() + "!")
print(len(input()))

# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇
c = a
a = b
b = c



# 🚨 Don't change the code below 👇
print("a: " + a)

#1. Create a greeting for your program.
print("Welcome to the Band Name Generator")
#2. Ask the user for the city that they grew up in.
city = input("What's the name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
pet_name = input("What's your pet's name?\n")
#4. Combine the name of their city and pet and show them their band name.
band_name = city + " " + pet_name
#5. Make sure the input cursor shows on a new line:
print("Your band name could be " + band_name)
# Solution: https://replit.com/@appbrewery/band-name-generator-end