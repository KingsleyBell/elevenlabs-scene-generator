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
    print(response.json())
    file_url = response.json()["fileUrl"]
    print("UPLOAD TMP FILE:", file_url)
    return file_url

