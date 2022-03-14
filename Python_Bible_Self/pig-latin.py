# Get sentence from user
original = input("Enter the sentence to conver into Pig Latin? :").strip().lower()

# Break the sentence into words
words = original.split()

# Loop through the words and convert into Pig Latin
new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word=word+"yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)
output=" ".join(new_words)
print(output)
print (original)
    
# Combine the words together to pig latin sentence


# Print the final sentence
