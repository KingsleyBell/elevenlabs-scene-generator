import datetime

from generators.video import generate_video
from generators.conversation import generate_conversation
from generators.sound_effect import generate_sound_effect

def generate_item(item: dict, files):
    if item["type"] == "VIDEO":
        return generate_video(files.get("file").read(), item["prompt"], int(item["duration"]))
    if item["type"] == "CONVERSATION":
        return generate_conversation(item["voice_id"], item["text"])
    if item["type"] == "SOUND_EFFECT":
        return generate_sound_effect(item["prompt"], item["duration"])


def generate(item, files):
    print(files)
    content = generate_item(item, files)

    output_dir = "output"
    output_base = f"{datetime.datetime.now().strftime('%Y%m%d-%H%M%S.%f')}"
    file_type = "mp4" if item["type"] == "VIDEO" else "mp3"
    file_name = f"{output_dir}/{output_base}.{file_type}"
    with open(file_name, "wb") as outfile:
        outfile.write(content)

    return f"{output_base}.{file_type}"

