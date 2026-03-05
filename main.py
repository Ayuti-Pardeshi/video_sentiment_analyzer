from src.transcript_extractor import get_transcript
from src.sentiment_model import analyze_sentiment

# this is the code i push today, it is working for putting youtube video link and getting the transcript and sentiment analysis of the transcript, it will print the first 10 sentences with their sentiment and confidence score.
def main():

    url = input("Enter YouTube URL: ")
    print("Extracting transcript...")


    transcript = get_transcript(url)
    print("Analyzing sentiment...")

    sentiments = analyze_sentiment(transcript)

    for result in sentiments[:10]:
        print("\nSentence:", result["sentence"])
        print("Sentiment:", result["label"])
        print("Confidence:", result["score"])
#calling main function

if __name__ == "__main__":
    main()
