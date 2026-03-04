from src.transcript_extractor import get_transcript
from src.sentiment_model import analyze_sentiment


def main():

    url = input("Enter YouTube URL: ")

    transcript = get_transcript(url)

    sentiments = analyze_sentiment(transcript)

    for result in sentiments[:10]:
        print("\nSentence:", result["sentence"])
        print("Sentiment:", result["label"])
        print("Confidence:", result["score"])


if __name__ == "__main__":
    main()