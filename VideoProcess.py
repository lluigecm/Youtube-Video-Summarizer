import moviepy.editor as mp
import speech_recognition as sr
from pytube import YouTube


def download_video(url: str, output : str = "video.mp4"):
    yt = YouTube(url)
    stream = yt.streams.get_lowest_resolution()
    stream.download(output_path = output)
    print("Downloaded video to " + output)
    return output


video = download_video("https://www.youtube.com/watch?v=d2uqo6PhdM4&t=2s")
