import datetime

from moviepy.editor import AudioFileClip, ColorClip

from pydub import AudioSegment

from utils.audio import get_audio_duration
from utils.video import get_video_duration


def sort_clips(clips):
    return sorted(clips, key=lambda x: float(x["start_time"]))


def get_total_video_duration(clips):
    last_clip = sort_clips(clips)[-1]
    return float(last_clip["start_time"]) + get_video_duration(f"output/{last_clip['file_name']}")


def get_total_audio_duration(clips):
    last_clip = sort_clips(clips)[-1]
    return float(last_clip["start_time"]) + get_audio_duration(
        f"output/{last_clip['file_name']}")


def get_total_duration(video_clips, audio_clips):
    return max(
        get_total_video_duration(video_clips),
        get_total_audio_duration(audio_clips)
    )


def create_video_canvas(duration):
    size = (1600, 900)
    color = (0, 0, 0)
    return ColorClip(size, color, duration=duration)


def create_audio_canvas(duration):
    canvas = AudioSegment.silent(duration=duration*1000)  # use default

    tmp_path = f"output/tmp/canvas-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S.%f')}.mp3"
    canvas.export(tmp_path, format="mp3")
    return AudioFileClip(tmp_path, fps=44100)
