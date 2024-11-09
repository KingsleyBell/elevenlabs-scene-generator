import os

import requests

bytescale_api_key = os.getenv("BYTESCALE_API_KEY")


def upload_file(content, content_type):
    url = "https://api.bytescale.com/v2/accounts/kW15cHW/uploads/binary"
    headers = {
        "Authorization": f"Bearer {bytescale_api_key}",
        "Content-Type": content_type
    }
    response = requests.post(url, headers=headers, data=content)
    file_url = response.json()["fileUrl"]
    return file_url

