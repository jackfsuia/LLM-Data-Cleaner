<p align="left">
    <img src="logo/logo.png" width="26%" >
</p>

# LLM-Data-Cleaner
English | [简体中文](README.md)
## Background
In future human will use LLM to preprocess all data. This project assembles LLMs and old tools to generate or clean data for academic use. For now it supports OCR, using various models like PaddleOCR(百度飞桨OCR), OpenAI, qwen(通义千问), moonshot(月之暗面).
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
## Examples
If you use qwen-vl-plus for OCR and your API key is sbadgassjda，the images data are in /images/，and the output `data.json`l is wished to be in /images/ too, whatever language is, run
```bash
python start_ocr.py --model qwen-vl-plus --key sbadgassjda --img_path /images/ --outdir /images/
```
If you use PaddleOCR, the images data are in /images/，and the output `data.json`l is wished to be in /images/ too, the OCR target language is English，run
```bash
python start_ocr --model paddle --img_path /images/ --outdir /images/ --lang en
```
## License

LLM-Data-Cleaner is licensed under the MIT License found in the [LICENSE](LICENSE) file in the root directory of this repository.
