import os

from dotenv import load_dotenv

from flask import Flask, request

from generators.engine import generate
from utils.file_upload import upload_file

app = Flask(__name__)
load_dotenv()

@app.route("/items", methods=["POST"])
def create_items():
    file_name = generate(request.form, request.files)

    return {"file_name": file_name}


@app.route("/items/<file_id>", methods=["GET"])
def get_item(file_id: str):
    file_path = f"output/{file_id}"
    if os.path.isfile(file_path):
        file_type = file_id.split(".")[-1]
        if file_type == "png":
            content_type = "image/png"
        elif file_type == "mp3":
            content_type = "audio/mpeg"
        elif file_type == "mp4":
            content_type = "video/mp4"

        content = open(file_path, "rb").read()
        image_url = upload_file(content, content_type)

        return {"url": image_url}
    return {}
