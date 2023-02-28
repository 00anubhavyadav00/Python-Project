from pytube import Playlist

link="https://www.youtube.com/playlist?list=PLUaB-1hjhk8GT6N5ne2qpf603sF26m2PW"
yt_playlist = Playlist(link)

for video in yt_playlist.videos:
    video.streams.get_highest_resolution().download()
    print(video.title)
