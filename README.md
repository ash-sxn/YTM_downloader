This project provides a set of scripts to automate the process of downloading MP3 versions of songs from YouTube Music. It uses the YTMusic API to retrieve video IDs and yt-dlp for downloading the audio in MP3 format.

Table of Contents
Introduction

Dependencies

Setup

Usage

Files

Examples

FAQ

Contributing

License

Introduction
This project automates the download of MP3 versions of songs from YouTube Music. It leverages the YTMusic API to find video IDs and uses yt-dlp to download the audio files.

Dependencies
Python 3.x: Available from the official website or via package manager.

ytmusicapi: Install using pip install ytmusicapi.

yt-dlp: Install using pip install yt-dlp or from the official GitHub repository.

Bash: Generally included in Unix-like operating systems.

Setup
Clone the repository:

bash
Copy
git clone https://github.com/ash-sxn/YTM_downloader.git
cd YTM_downloader
Install dependencies:

bash
Copy
pip install ytmusicapi yt-dlp
Prepare input files:

Create needed_songs.txt and add the names of the songs you want to download.

Create downloaded_ids.txt if not already present (it can be empty initially).

Usage
Edit needed_songs.txt to include the list of songs, one per line.

Run the Python script:

bash
Copy
python download_songs.py
This script will:

Read the list of needed songs.

Read the list of downloaded video IDs.

Find which songs still need to be downloaded.

Search for their video IDs on YouTube Music.

Write the video IDs to song_ids.txt.

Call the bash script to download the MP3s.

Update downloaded_ids.txt with the new video IDs.

The bash script audoytdlp.sh will download the MP3s and save them to the Music_mp3 directory.

Files
download_songs.py: The main script that coordinates the process.

audoytdlp.sh: The bash script that downloads the MP3s.

needed_songs.txt: Input file with the list of songs to download.

downloaded_ids.txt: Keeps track of video IDs that have been downloaded.

remaining_songs.txt: Automatically generated list of songs still needing download.

song_ids.txt: List of video IDs for the remaining songs.

Examples
Sample content for needed_songs.txt:

Copy
Song Name 1
Song Name 2
Song Name 3
After running the scripts, MP3 files of these songs will be in the Music_mp3 directory.

FAQ
Q: What if a song isn't found on YouTube Music?

A: The script will skip that song and print an error message.

Q: How do I handle errors during download?

A: Check the error messages and ensure that yt-dlp is installed and that you have internet access.

Q: Can I download multiple songs at once?

A: The bash script can be modified to download multiple songs in parallel by using tools like xargs with the -P option.

Contributing
Contributions are welcome! If you find a bug or want to add a new feature, please open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

