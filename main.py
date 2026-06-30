from textblob import TextBlob

print("===== AI Sentiment Analyzer =====")

while True:
    text = input("\nEnter a sentence (or type quit): ")

    if text.lower() == "quit":
        print("Goodbye!")
        break

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    print(f"Polarity Score: {polarity:.2f}")

    if polarity > 0:
        print("Sentiment: Positive 😊")
    elif polarity < 0:
        print("Sentiment: Negative 😔")
    else:
        print("Sentiment: Neutral 😐")
