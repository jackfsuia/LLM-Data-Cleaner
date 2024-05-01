# LLM-Data-Cleaner

[English](README_en.md) | 简体中文

用大模型来批量预处理数据，以支持科研目的。 现阶段支持OCR功能, 支持使用的大模型有 qwen(通义千问), moonshot(月之暗面), PaddleOCR(百度飞桨OCR), openai。
## 启动
克隆并且进入仓库
```bash
git clone https://github.com/jackfsuia/LLM-Data-Cleaner.git && cd LLM-Data-Cleaner
```
进入仓库然后跑下面命令启动OCR
```bash
python start_ocr.py --model MODEL --key YOUR_API_KEY --img_path /path/to/images/ --outdir /path/to/output/ --lang language
```
**MODEL** 的值可以是 "qwen"(通义千问), "moonshot"(月之暗面), "paddle"(百度飞桨OCR), "openai". **YOUR_API_KEY** 是你申请的API KEY, paddle不需要。 **/path/to/images/** 是图片目录, 里面所有图片都会被OCR, 生成的文件是 **/path/to/output/** data.jsonl。 **language** 是识别的语言，值可以是 ch (中文), en (英文), fr (法语), german (德语), korean (韩语), japan (日语), 只有百度飞桨OCR可能会用到。

## 许可

项目许可证是[LICENSE](LICENSE)。
