import cv2


def get_video_duration(content_or_url):
    data = cv2.VideoCapture(content_or_url)

    frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = data.get(cv2.CAP_PROP_FPS)

    duration = round(frames / fps)
    return duration
