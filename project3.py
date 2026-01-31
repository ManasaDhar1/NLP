spam_words = ["win","prize","free","cash"]
text = "You are WINNING a PRIZE now"
text = text.lower()
for word in text:
    if word in text:
        print("spam message")
        break
    else:
        print("not spam message")
