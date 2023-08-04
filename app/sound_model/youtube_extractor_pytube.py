from pytube import YouTube
from moviepy.editor import AudioFileClip

#placeholder for id
id = "cFRWskjVOyc"

#get video and audio
video = YouTube('https://www.youtube.com/watch?v=cFRWskjVOyc')
audio = video.streams.filter(only_audio = True, file_extension = 'mp4').first()

title = video.title
filename =  title + ".mp4"

#download audio
audio.download(output_path='app/test_data/', filename=filename)

clip = AudioFileClip("app/test_data/" + filename)
clip.write_audiofile(f"app/test_data/{title}.wav", fps=16000)
