from paddleocr import PaddleOCR, draw_ocr
from models.ocr import base_ocr

class paddle_ocr(base_ocr):
    def __init__(self, lang):
        super().__init__()
        self.lang=lang
    def ocr_image(self, img_path):
        # Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
        # 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
        text=""
        pocr = PaddleOCR(use_angle_cls=True, lang=self.lang)  # need to run only once to download and load model into memory
        result = pocr.ocr(img_path, cls=True)
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                text=text+line[1][0]+'\n'
        return text
