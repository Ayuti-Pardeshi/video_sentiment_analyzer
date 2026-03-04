import yt_dlp
import whisper
import os


def download_audio(url):
    """
    Download audio from YouTube using yt-dlp
    """

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'data/audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return "data/audio.mp3"


def transcribe_audio(audio_path):
    """
    Convert speech to text using Whisper
    """

    model = whisper.load_model("base")

    result = model.transcribe(audio_path)

    return result["text"]


def get_transcript(url):

    audio_path = download_audio(url)

    transcript = transcribe_audio(audio_path)

    return transcript