numbers = input('Enter numbers :')
words={
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight"
}
output = ""
for char in numbers:
    output += words.get(char, "?")+" "
print(output)