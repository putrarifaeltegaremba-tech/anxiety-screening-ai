from textblob import TextBlob

def analyze_text(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity < -0.3:
        return "Negatif"
    elif polarity < 0.3:
        return "Netral"
    else:
        return "Positif"
