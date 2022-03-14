vowels=0
consonents=0
a=input("Tell me the word and I will count vowels and consonents in it? :").strip().capitalize()

for letter in a:

    if letter.lower() in "aeiou":
        vowels=vowels+1

    elif letter==" ":
        pass

    else:
        consonents=consonents+1

print("There are {} vowels ".format(vowels))
print("There are {} consonents ".format(consonents))

            
