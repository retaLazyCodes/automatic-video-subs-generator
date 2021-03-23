from moviepy.editor import AudioClip, VideoClip, VideoFileClip
import os
import fnmatch


def get_directory():
    f = open('path.txt', 'r')
    return f.read()


def set_directory(actual_directory):
    directory = actual_directory.replace('\\', '\\\\')
    with open('path.txt', 'w') as file:
        file.write(directory)


def get_all_videos():
    return fnmatch.filter(os.listdir(get_directory()), '*.mp4')


def convert_video_to_audio():
    video_list = get_all_videos()

    for video_file in video_list:
        video_route = get_directory() + '\\' + video_file
        audio_file = video_route.replace('mp4', 'mp3')
        VideoClip = VideoFileClip(video_route)
        AudioClip = VideoClip.audio
        AudioClip.write_audiofile(audio_file)

        AudioClip.close()
        VideoClip.close()
