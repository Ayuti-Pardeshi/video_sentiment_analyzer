from transformers import pipeline
import nltk

nltk.download('punkt')


# Load sentiment model
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)


def analyze_sentiment(text):

    sentences = nltk.sent_tokenize(text)

    results = []

    for sentence in sentences:
        sentiment = sentiment_pipeline(sentence)[0]

        results.append({
            "sentence": sentence,
            "label": sentiment["label"],
            "score": sentiment["score"]
        })

    return results