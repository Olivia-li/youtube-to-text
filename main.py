import whisper
from youtube import get_video_urls, download_youtube_mp3
from os import walk
from tqdm.auto import tqdm

YOUTUBE_URL_FILE = "data/video_urls.json"
model = whisper.load_model("base")

# video_urls = get_video_urls(YOUTUBE_URL_FILE)
# download_youtube_mp3(video_urls, "data/audio")

audio_files = []
for (dirpath, dirnames, filenames) in walk("data/audio"):
    audio_files.extend(filenames)
    break

for audio_path in tqdm(audio_files):
    result = model.transcribe(f"./data/audio/{audio_path}")
    text_name = audio_path.split(".")[0] + ".txt"
    print(f"{audio_path}: Finished")
    with open(f'data/transcriptions/{text_name}', 'w') as f:
        f.write(result["text"])