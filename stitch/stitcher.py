import datetime

from moviepy.editor import (
    AudioFileClip,
    CompositeAudioClip,
    CompositeVideoClip,
    VideoFileClip,
)

from stitch.utils import (
    create_audio_canvas,
    create_video_canvas,
    get_total_duration,
)


def stitch(clips):
    video_clips = [clip for clip in clips if clip["file_name"].endswith(".mp4")]
    audio_clips = [clip for clip in clips if clip["file_name"].endswith(".mp3")]
    total_duration = get_total_duration(video_clips, audio_clips)

    video = stitch_video(video_clips, total_duration)
    audio = stitch_audio(audio_clips, total_duration)

    video = video.set_audio(audio)

    output_base = f"{datetime.datetime.now().strftime('%Y%m%d-%H%M%S.%f')}"
    file_path = f"output/final_video_{output_base}.mp4"
    video.write_videofile(file_path, audio_codec="aac")

    return file_path


def stitch_video(clips, total_duration):
    canvas = create_video_canvas(total_duration)

    for clip in clips:
        canvas = add_video_clip(canvas, clip)

    return canvas


def add_video_clip(canvas, clip):
    file_clip = VideoFileClip(f"output/{clip['file_name']}", audio=False)
    file_clip = file_clip.resize(width=1600, height=900)
    file_clip = file_clip.set_start(float(clip["start_time"]))
    return CompositeVideoClip([canvas, file_clip])


def stitch_audio(clips, total_duration):
    canvas = create_audio_canvas(total_duration)

    audio_clips = [canvas]
    for clip in clips:
        audioclip = AudioFileClip(f"output/{clip['file_name']}", fps=44100)
        audio_clips.append(audioclip.set_start(float(clip["start_time"])))

    return CompositeAudioClip(audio_clips)
