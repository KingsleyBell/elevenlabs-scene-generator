from pydub import AudioSegment


def get_audio_duration(file_path):
    return AudioSegment.from_mp3(file_path).duration_seconds

