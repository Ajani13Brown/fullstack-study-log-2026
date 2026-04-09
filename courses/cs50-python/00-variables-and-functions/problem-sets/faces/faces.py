def convert(text):
    new_text = text.replace(":)", "🙂").replace(":(", "🙁")
    return new_text

smile_text = input("What would you like to say?\n")

print(convert(smile_text))
