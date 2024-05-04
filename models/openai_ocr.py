import base64
import requests
from ocr import base_ocr



class openai_ocr(base_ocr):
    def __init__(self, MODEL, KEY):
        super().__init__()
        if MODEL == 'openai':
            MODEL='gpt-4-turbo'
        self.MODEL=MODEL
        self.api_key = KEY

    def ocr_image(self, image_path):

        # Function to encode the image
        def encode_image(image_path):
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')

        # Path to your image
        # Getting the base64 string
        base64_image = encode_image(image_path)

        headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
        "model": self.MODEL,
        "messages": [
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": self.prompt
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
                }
            ]
            }
        ],
        "max_tokens": 300
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        # to be done...
        return str(response.json())



