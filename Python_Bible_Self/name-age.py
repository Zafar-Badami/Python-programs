# Create a variable called name and set it equal to your name

name="Zafar"
# Create a variable called age and set it equal to your age
age=49
numbers = [1,2,3,4,5]
for number in numbers:
    print(number)
# Create a variable called output, and use {} symbols and the format() function to 
# make it contain a string like the example text in the description
string="My name is {} and I am {} years old"
output=string.format(name,age)
# Finally, use the print() function to print the output.
print(output)
print("")
class Point:
    def move(self)