import requests
from typing import Optional

import requests
from typing import Optional

class Webhook:
    def __init__(self, url: str, default_username: Optional[str] = None, default_avatar_url: Optional[str] = None):
        self.url = url
        self.default_username = default_username
        self.default_avatar_url = default_avatar_url or "https://em-content.zobj.net/source/apple/419/shark_1f988.png"

    def send_message(self, content: str, toggle: Optional[bool] = True, username: Optional[str] = None, avatar_url: Optional[str] = None):
        if toggle:
            data = {
                "content": content,
                "username": username or self.default_username,
                "avatar_url": avatar_url or self.default_avatar_url
            }

            data = {k: v for k, v in data.items() if v is not None}

            response = requests.post(self.url, json=data)

            if response.status_code != 204:
                raise Exception(f"Failed to send webhook: {response.status_code}, {response.text}")