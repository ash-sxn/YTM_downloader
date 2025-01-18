from ytmusicapi import YTMusic
import subprocess

def main():
    needed_songs_file = 'needed_songs.txt'
    downloaded_ids_file = 'downloaded_ids.txt'
    remaining_songs_file = 'remaining_songs.txt'
    song_ids_file = 'song_ids.txt'
    output_dir = 'Music_mp3'

    # Read needed songs and downloaded IDs
    with open(needed_songs_file, 'r', encoding='utf-8') as f:
        needed_songs = set(line.strip() for line in f if line.strip())

    with open(downloaded_ids_file, 'r', encoding='utf-8') as f:
        downloaded_ids = set(line.strip() for line in f if line.strip())

    # Find remaining songs
    remaining_songs = needed_songs - set(downloaded_ids)
    with open(remaining_songs_file, 'w', encoding='utf-8') as f:
        for song in remaining_songs:
            f.write(song + '\n')

    # Retrieve video IDs for remaining songs
    ytmusic = YTMusic()
    with open(song_ids_file, 'w', encoding='utf-8') as f:
        for song_name in remaining_songs:
            try:
                search_results = ytmusic.search(song_name, filter='songs')
                if search_results:
                    video_id = search_results[0]['videoId']
                    f.write(video_id + '\n')
                    print(f"Found ID for '{song_name}': {video_id}")
                else:
                    print(f"No results found for '{song_name}'")
            except Exception as e:
                print(f"Error searching for '{song_name}': {e}")

    # Call the bash script to download MP3s
    subprocess.call(['bash', 'audoytdlp.sh'])

    # Update downloaded_ids.txt with new video IDs
    with open(song_ids_file, 'r', encoding='utf-8') as f:
        new_ids = set(line.strip() for line in f if line.strip())

    with open(downloaded_ids_file, 'a', encoding='utf-8') as f:
        for video_id in new_ids:
            f.write(video_id + '\n')

if __name__ == "__main__":
    main()
