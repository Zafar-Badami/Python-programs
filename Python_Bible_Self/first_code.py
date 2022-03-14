# first ask name
name = input("Your name ?: ")
# ask for age 
age = input("Your age ?: ")
# ask user for city
city = input("Your city ?: ")
# ask user what they enjoy
hobby = input("Your hobby ?: ")
# Create output text
string = "My name is {}, I am {} years old, live in {} and enojoy {} "
output = string.format(name,age,city,hobby)
# print the output
print(output)
