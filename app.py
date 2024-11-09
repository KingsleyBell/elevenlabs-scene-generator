import os

from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS

from generators.engine import generate
from stitch.stitcher import stitch
from utils.file_upload import upload_file

app = Flask(__name__)
CORS(app)
load_dotenv()


@app.route("/items", methods=["POST", "OPTIONS"])
def create_items():
    if request.method == "OPTIONS":
        return {}
    
    file_name = generate(request.form, request.files)

    return {"file_name": file_name}


@app.route("/items/<file_id>", methods=["GET", "OPTIONS"])
def get_item(file_id: str):
    if request.method == "OPTIONS":
        return {}
    
    file_path = f"output/{file_id}"
    if os.path.isfile(file_path):
        file_type = file_id.split(".")[-1]
        content_type = None
        
        if file_type == "png":
            content_type = "image/png"
        elif file_type == "mp3":
            content_type = "audio/mpeg"
        elif file_type == "mp4":
            content_type = "video/mp4"
            
        if content_type is None:
            return {"error": "Unsupported file type"}, 400

        content = open(file_path, "rb").read()
        image_url = upload_file(content, content_type)

        return {"url": image_url}
    return {}


@app.route("/items", methods=["POST", "OPTIONS"])
def stitch_items():
    if request.method == "OPTIONS":
        return {}

    file_name = stitch(request.form)
    return {"file_name": file_name}
