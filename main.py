from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=NjvwWiCYLl4&ab_channel=JonathanArrington')

streams = yt.streams.filter(progressive=True)

resolutions = []
for stream in streams:
    resolutions.append(stream.resolution)
print(resolutions)

