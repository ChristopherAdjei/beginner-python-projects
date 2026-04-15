def emoji_conv(message):
    words = message.split(" ")
    emojis = {":)": "😊", ":(": "😒"}

    output = ""
    for word in words:
        output = output + emojis.get(word, word) + " "
    return output


message = input(">")
result = emoji_conv(message)
print(result)