import argparse
import json
import os

def OCR_the_dataset(ocr_img, folder_path, outdir):
    current_dir_path = os.path.dirname(os.path.abspath(__file__))
    if outdir == None:
        outdir=current_dir_path
    if folder_path == None:
        folder_path=current_dir_path
    file_name = os.path.join(outdir, "data.jsonl")
    with open(file_name, 'w', encoding='utf-8') as jsonl_file:##
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".tif") or filename.endswith(".jpeg"):
                img_path = os.path.join(folder_path, filename)
                item={}
                item["name"]=filename
                ocr_result=ocr_img(img_path)
                if ocr_result:
                    item["ocr_result"]= ocr_result
                    jsonl_file.write(json.dumps(item) + '\n')

    print(f"data has been written to {file_name}")    


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="ocr")
    
    parser.add_argument('--model', type=str, help="model name")
    parser.add_argument('--key', type=str, help="api key")
    parser.add_argument('--img_path', type=str, help="images folder path")
    parser.add_argument('--outdir', type=str, help="output dir")
    parser.add_argument('--lang', default='en',type=str, help="language:`ch`, `en`, `fr`, `german`, `korean`, `japan`")
    
    args = parser.parse_args()
    

    model = args.model
    key= args.key
    img_path=args.img_path
    outdir=args.outdir
    lang=args.lang
    if model.startswith("qwen"):
        from models import qwen_ocr
        ocr_img = qwen_ocr.qwen_ocr(model, key).closuer_ocr_image()
    elif model.startswith("kimi") or model.startswith("moonshot"):
        from models import kimi_ocr
        ocr_img = kimi_ocr.kimi_ocr(model, key).closuer_ocr_image()
    elif model=='paddle':
        from models import paddle_ocr
        ocr_img = paddle_ocr.paddle_ocr(lang).closuer_ocr_image()
    elif model == 'openai' or model.startswith("gpt"):
        from models import openai_ocr
        ocr_img = openai_ocr.openai_ocr(model, key).closuer_ocr_image()
    elif "llava" in model.lower():
        from models import llava_ocr
        ocr_img = llava_ocr.llava_ocr(model).closuer_ocr_image()
    else:
        raise Exception("This model has not been supported.")
    
    OCR_the_dataset(ocr_img, img_path, outdir)





