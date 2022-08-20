"""
実行時注意点
・ファイルパスは半角ローマ字だけを含む
・Cドライブが存在する
"""


import tkinter.filedialog
from pathlib import Path
import PyPDF2


# 結合させるpdfファイルが入っているフォルダをファイルダイアログにて選択
idir = 'C:'
pdf_dir = tkinter.filedialog.askdirectory(initialdir = idir)

# フォルダ内のPDFファイルを昇順でリスト化
pdf_files = sorted(Path(pdf_dir).glob("*.pdf"))

# PDFファイルを結合する
pdf_writer = PyPDF2.PdfFileWriter()
for pdf_file in pdf_files:
    pdf_reader = PyPDF2.PdfFileReader(str(pdf_file))
    for i in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(i))

# 保存ファイル名（先頭と末尾のファイル名で作成）
merged_file = pdf_dir + "\仮"  + ".pdf"

# 保存
with open(merged_file, "wb") as f:
    pdf_writer.write(f)



