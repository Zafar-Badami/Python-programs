def emoji_converter(message):
    emoji={
    ":(":"😔",
    ":)":"😊"
    }
    sentence=""
    list=message.split(" ")
    for word in list:
        sentence +=emoji.get(word,word)+ " "
    return sentence
message = input(" > ")
sentence = emoji_converter(message)
print(sentence)