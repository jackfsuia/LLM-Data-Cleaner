# LLM-Data-Cleaner

English | [简体中文](README.md)
## Background
In future human will use LLM to preprocess all data. This project assembles LLMs and old tools to generate or clean data for academic use. For now it supports OCR, using various models like qwen(通义千问), moonshot(月之暗面), PaddleOCR(百度飞桨OCR), openai.
## Start
Clone and enter the repo
```bash
git clone https://github.com/jackfsuia/LLM-Data-Cleaner.git && cd LLM-Data-Cleaner
```
then to start OCR, run 
```bash
python start_ocr.py --model MODEL --key YOUR_API_KEY --img_path /path/to/images/ --outdir /path/to/output/ --lang language
```
**MODEL** can be ["qwen"](https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key), ["moonshot"](https://platform.moonshot.cn/console/api-keys), ["paddle"](https://github.com/PaddlePaddle/PaddleOCR), ["openai"](https://platform.openai.com/docs/models/overview). **YOUR_API_KEY** is the API KEY, not needed for paddle. **/path/to/images/** is the images folder, it will ocr all the images under that path, and save the result to the file **/path/to/output/** data.jsonl. **language** can be ch (Chinese), en (English), fr (French), german (German), korean (Korean), japan (Japanese), it is only used by paddle.

## License

LLM-Data-Cleaner is licensed under the MIT License found in the [LICENSE](LICENSE) file in the root directory of this repository.
