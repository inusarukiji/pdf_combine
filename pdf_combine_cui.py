from pathlib import Path
import PyPDF2
import sys

# フォルダ内のPDFファイルを昇順でリスト化
pdf_dir = Path(str(sys.argv[1]))
pdf_files = sorted(pdf_dir.glob("*.pdf"))

print(pdf_dir)

# PDFファイルを結合する
pdf_writer = PyPDF2.PdfFileWriter()
for pdf_file in pdf_files:
    pdf_reader = PyPDF2.PdfFileReader(str(pdf_file))
    for i in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(i))

# 保存ファイル名（先頭と末尾のファイル名で作成）
merged_file = str(sys.argv[1]) + "\仮"  + ".pdf"

print(merged_file)

# 保存
with open(merged_file, "wb") as f:
    pdf_writer.write(f)