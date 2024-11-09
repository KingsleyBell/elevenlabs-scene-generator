import requests

# Get file
file_path = "20241109-150557-0.mp3"
url = f"http://127.0.0.1:5000/item/{file_path}"
response = requests.get(url)

# Create video
url = "http://127.0.0.1:5000/items"
data = {
    "type": "VIDEO",
    "prompt": "people flying kites in the park",
    "duration": 3,
}
files = {"file": open("8.png", "rb").read()}
response = requests.post(url, data=data, files=files)

# Create conversation

# Create
