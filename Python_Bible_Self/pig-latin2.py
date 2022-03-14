# Get sentence from user

original =input("Please enter your sentence for convertion? :").strip().lower()

# Break the sentence into words
words = original.split()

# Loop through the words and convert into Pig Latin
new_words = []
for word in words:

    if word[0] in "aeiou":
        word=word+"yay"
        new_words.append(word)

    else:
        vowel_pos=0

        for letter in word:
            if letter not in "aeiou":
                vowel_pos=vowel_pos+1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

output = " ".join(new_words)
print(output)


# Rules: 1. if starts with vowel add "yay" at the end
#            2. Otherwise , move first consonant cluster to end and add "ay"
# Combine the words together to pig latin sentence

# Stick words back together

# Print the final sentence
