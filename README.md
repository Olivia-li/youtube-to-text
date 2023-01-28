# youtube-to-text
Transcribe any YouTube video using OpenAI Whisper

## Setup 
1) Download your Python dependencies `pip3 install -r requirements.txt`
2) Whisper depends on ffmpeg.<br>
```
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

## Transcribe any Youtube file
In `video_urls.json` replace the filler links with the urls of the YouTube videos that you want to download.<img width="514" alt="image" src="https://user-images.githubusercontent.com/9896624/215282570-cc3b53a4-fc95-4157-8a30-e421f4f9aa13.png">

Run `python3 main.py` to transcribe your YouTube videos. The `.txt` files will save to the `data/text` folder
