from PyPDF2 import PdfFileReader
import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LTTextLine, LAParams, LTPage
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfdevice import PDFDevice


def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    output = io.StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    return text


f = open('vod sample.pdf', 'rb')
reader = PdfFileReader(f)
contents = reader.getPage(0).extractText()  # .split('\n')
print("Number of pages in pdf file:", reader.getNumPages())
print('Title:', reader.documentInfo['/Title'])
print('Author:', reader.documentInfo['/Author'])
print('Producer:', reader.documentInfo['/Producer'])
# p_text = reader.getPage(0).extractText()
# p_lines = p_text.splitlines()
# print(p_lines)
pdf_text = convert('vod sample.pdf', pages=[0]).split('\n')
print(pdf_text)
for w in pdf_text: print(w)
f.close()
