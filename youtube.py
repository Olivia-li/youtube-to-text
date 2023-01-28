from pytube import YouTube 
from pytube.exceptions import RegexMatchError
from tqdm.auto import tqdm
import json

# load the video urls
def get_video_urls(url_file):
    with open(url_file, "r") as f:
        return  json.load(f)

# download the videos
def download_youtube_mp3(video_urls, output_path):
    print(video_urls)
    for url in tqdm(video_urls):
        try:
            yt = YouTube(url)
        except RegexMatchError:
            print(f"RegexMatchError for '{url}'")
            continue

        itag = None
        files = yt.streams.filter(only_audio=True)
        for file in files:
            if file.mime_type == 'audio/mp4':
                itag = file.itag
                break
        if itag is None:
            print("NO MP3 AUDIO FOUND")
            continue

        stream = yt.streams.get_by_itag(itag)
        stream.download(
            output_path=f"{output_path}.mp3",
            filename=yt.streams[0].title
        )