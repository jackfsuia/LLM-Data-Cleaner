from http import HTTPStatus
import dashscope
from ocr import base_ocr

class qwen_ocr(base_ocr):
    def __init__(self, MODEL, KEY):
        super().__init__()
        if MODEL == 'qwen':
            MODEL='qwen-vl-plus'
        self.MODEL=MODEL
        dashscope.api_key = KEY

    def ocr_image(self, img):

        messages = [
            {
                "role": "user",
                "content": [
                    {"image": f"file://{img}"},
                    {"text": self.prompt}
                ]
            }
        ]
        response = dashscope.MultiModalConversation.call(model=self.MODEL,messages=messages)

        if response.status_code == HTTPStatus.OK:
            return response.output.choices[0].message.content
        else:
            print(response.code)  # The error code.
            print(response.message)  # The error message.
            return None

    
  
