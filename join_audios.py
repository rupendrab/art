from pydub import AudioSegment
# import os
# ffmpeg_path='/Users/rupen/Downloads'
# os.environ["PATH"] += os.pathsep + ffmpeg_path

def combine_audio_files(file1, file2, output_file):
    audio1 = AudioSegment.from_mp3(file1)
    audio2 = AudioSegment.from_mp3(file2)
    combined = audio1 + audio2
    combined.export(output_file, format='mp3')

# Example usage
file1 = '/Users/rupen/downloads/part_1.mp3'
file2 = '/Users/rupen/downloads/part_2.mp3'
output_file = '/Users/rupen/downloads/combined.mp3'

combine_audio_files(file1, file2, output_file)
