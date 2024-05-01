
class base_ocr:

    def __init__(self) -> None:
        self.prompt = "把里面的文字、每一条公式都原封不动、不带翻译地提取出来。你的回答应该直接是结果，不用你其他多余的说明。"
    def ocr_image(self,img):
        pass

    def closuer_ocr_image(self):

        def ocr_image(img):
            return self.ocr_image(img)
        
        return ocr_image

    
   