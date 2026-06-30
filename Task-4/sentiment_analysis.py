import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

df = pd.read_csv("reviews.csv")

def analyze_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Review"].apply(analyze_sentiment)

df.to_csv("results.csv", index=False)

sentiment_counts = df["Sentiment"].value_counts()

print(sentiment_counts)

sentiment_counts.plot(kind="bar")
plt.title("Sentiment Analysis Results")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.savefig("sentiment_chart.png")
plt.show()