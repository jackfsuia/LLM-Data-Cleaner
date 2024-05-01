from models.ocr import base_ocr
from pathlib import Path
from openai import OpenAI


class kimi_ocr(base_ocr):
    def __init__(self, MODEL, KEY):
        super().__init__()
        if MODEL == "kimi":
            MODEL = "moonshot-v1-32k"
        self.client = OpenAI(
            api_key=KEY,
            base_url="https://api.moonshot.cn/v1",
        )
        self.MODEL=MODEL

    def ocr_image(self, img):
        # xlnet.pdf 是一个示例文件, 我们支持 pdf, doc 以及图片等格式, 对于图片和 pdf 文件，提供 ocr 相关能力
        file_object = self.client.files.create(file=Path(img), purpose="file-extract")
       
        file_content = self.client.files.content(file_id=file_object.id).text

        # 把它放进请求中
        messages = [
            {
                "role": "system",
                "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。",
            },
            {
                "role": "system",
                "content": file_content,
            },
            {"role": "user", "content": self.prompt},
        ]

        # 然后调用 chat-completion, 获取 Kimi 的回答
        completion = self.client.chat.completions.create(
        model= self.MODEL,
        messages=messages,
        temperature=0.3,
        )

        return completion.choices[0].message.content