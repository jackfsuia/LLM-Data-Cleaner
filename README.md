# LLM-Data-Cleaner

English | [简体中文](README_zh.md)

Use LLM to generate or clean data for academic use. For now it supports OCR, using various models like qwen(通义千问), moonshot(月之暗面), PaddleOCR(百度飞桨OCR), openai.
## Start
Clone the repo
```bash
git clone https://github.com/jackfsuia/LLM-Data-Cleaner.git
```
then to start OCR, run 
```bash
python start_ocr.py --model MODEL --key YOUR_API_KEY --img_path /path/to/images/ --outdir /path/to/output/ --lang language
```
**MODEL** can be "qwen", "moonshot", "paddle", "openai". **YOUR_API_KEY** is the API KEY, not needed for paddle. **/path/to/images/** is the images folder, it will ocr all the images under that path, and save the result to the file **/path/to/output/**data.jsonl. **language** can be ch (Chinese), en (English), fr (French), german (German), korean (Korean), japan (Japanese), it is only used by paddle.

## License

ShampooSalesAgent is licensed under the MIT License found in the [LICENSE](LICENSE) file in the root directory of this repository.
