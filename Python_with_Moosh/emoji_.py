def emoji_converter(message):
    words = message.split(' ')
    emoji = {
         ":)":"happy_face",
         ":(":"sad_face"
    }
    output=""
    for word in words:
        output += emoji.get(word, word)+" "
    return output


message = input(">")
print(emoji_converter(message))