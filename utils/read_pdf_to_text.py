import pdfplumber

import os
def extract_txt_from_pdf(fn, tgt_path):
    """
    Extract text from a pdf file and save to target path.

    :param fn: path to input pdf file
    :param tgt_path: path to save text file.
    """
    with pdfplumber.open(fn) as pdf:
        text = []
        for page in pdf.pages:
            # remove tables from each page extracted by pdfplumber
            tables = page.find_tables()
            for table in tables:
                page = page.outside_bbox(table.bbox)
            # remove page number from the end of each page
            page_text = page.extract_text()
            page_num = str(page.page_number)
            if page_text.rstrip().endswith(page_num):
                page_text = page_text.rstrip()[:-len(page_num)]
            if page_text.strip():
                text.append(page_text)
        base_fn = os.path.basename(fn).lower().replace('.pdf', '.txt')
        with open(os.path.join(tgt_path, base_fn), 'w', encoding='utf-8') as f:
            f.write('\n'.join(text))

extract_txt_from_pdf("C:\\Users\\Administrator\\Desktop\\CVX.pdf", "C:\\Users\\Administrator\\Desktop")