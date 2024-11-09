import os

import requests
import time

import cv2
from lumaai import LumaAI
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from utils.file_upload import upload_file

box_api_key = os.getenv("BOX_API_KEY")
luma_api_key = os.getenv("LUMA_API_KEY")

def generate_video(image_content, prompt, duration):
    image_url = upload_file(image_content, "image/png")
    base_generation = generate_video_base(image_url, prompt)

    generation_duration = get_generation_video_duration(base_generation)

    while generation_duration < duration:
        base_generation = extend_generation_video(base_generation)
        generation_duration = get_generation_video_duration(base_generation)

    return trim_generation_video(base_generation, duration)


def generate_video_base(image_url, prompt):
    client = LumaAI(auth_token=luma_api_key)

    generation = client.generations.create(
        prompt=prompt,
        keyframes={
            "frame1": {
                "type": "image",
                "url": image_url,
            },
        }
    )

    completed = False
    while not completed:
        generation = client.generations.get(id=generation.id)
        if generation.state == "completed":
            completed = True
        elif generation.state == "failed":
            raise RuntimeError(f"Generation failed: {generation.failure_reason}")
        print("Generating video")
        time.sleep(3)

    return generation


def get_generation_video_duration(generation):
    data = cv2.VideoCapture(generation.assets.video)

    frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = data.get(cv2.CAP_PROP_FPS)

    duration = round(frames / fps)
    print("DURATION:", duration)
    return duration


def extend_generation_video(generation):
    client = LumaAI(auth_token=luma_api_key)

    generation = client.generations.create(
        prompt=generation.request.prompt,
        keyframes={
            "frame1": {
                "type": "generation",
                "id": generation.id,
            },
        }
    )

    completed = False
    while not completed:
        generation = client.generations.get(id=generation.id)
        if generation.state == "completed":
            completed = True
        elif generation.state == "failed":
            raise RuntimeError(f"Generation failed: {generation.failure_reason}")
        print("Extending Video")
        time.sleep(3)

    return generation


def trim_generation_video(generation, duration):
    video_url = generation.assets.video
    content = requests.get(video_url, stream=True).content

    tmp_output_path = f"output/tmp/{generation.id}.mp4"
    tmp_output_path_trimmed = f"output/tmp/{generation.id}-trimmed.mp4"

    with open(tmp_output_path, "wb") as tmp_file:
        tmp_file.write(content)

    ffmpeg_extract_subclip(tmp_output_path, 0, duration, targetname=tmp_output_path_trimmed)

    return open(tmp_output_path_trimmed, "rb").read()
