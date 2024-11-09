import requests

# Get file
file_path = "20241109-172858.167135.mp3"
url = f"http://127.0.0.1:5000/items/{file_path}"
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
url = "http://127.0.0.1:5000/items"
data = {
    "type": "CONVERSATION",
    "voice_id": "pNInz6obpgDQGcFmaJgB",
    "text": "Hello my name is Bob",
}
response = requests.post(url, data=data)

# Create sound effect
url = "http://127.0.0.1:5000/items"
data = {
    "type": "SOUND_EFFECT",
    "prompt": "city cars",
    "duration": 10,
}
response = requests.post(url, data=data)
