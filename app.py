import os

from flask import Flask, request

from generators.engine import generate

app = Flask(__name__)


@app.route("/items", methods=["POST"])
def create_items():
    file_name = generate(request.form, request.files)

    return {"file_name": file_name}


@app.route("/items/<file_id>", methods=["GET"])
def get_item(file_id: str):
    file_path = f"output/{file_id}"
    if os.path.isfile(file_path):
        return {"file": str(open(file_path, "rb").read())}
    return {}
