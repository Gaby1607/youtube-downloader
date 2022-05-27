import re
from pytube import Playlist
import os
fisier = input('Locatia de download\n')
YOUTUBE_STREAM_AUDIO = '140'
DOWNLOAD_DIR = fisier

linkPlaylist = input('Link ul playlistului\n')
playlist =  Playlist(linkPlaylist)

playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print (len(playlist.video_urls))

for url in playlist.video_urls:
    print(url)

for video in playlist.videos:
    audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
    audioStream.download(output_path=DOWNLOAD_DIR)
    out_file = audioStream.download(output_path=DOWNLOAD_DIR)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)