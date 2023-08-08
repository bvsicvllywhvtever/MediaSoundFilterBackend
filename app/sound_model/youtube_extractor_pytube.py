from pytube import YouTube
from moviepy.editor import AudioFileClip

def extract_audio(id):

    #get video and audio
    video = YouTube('https://www.youtube.com/watch?v=' + id)
    audio = video.streams.filter(only_audio = True, file_extension = 'mp4').first()

    title = id
    filename =  title + ".mp4"

    #download audio
    audio.download(output_path='sound_model/test_data/', filename=filename)

    clip = AudioFileClip("sound_model/test_data/" + filename)
    clip.write_audiofile(f"sound_model/test_data/{title}.wav", fps=16000)
