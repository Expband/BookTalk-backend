from fastapi import File, UploadFile
from pdfquery import PDFQuery
from io import BytesIO
from .IDriver import IDriver


class PdfDriver(IDriver):
    @staticmethod
    async def read(file: UploadFile = File(...)):
        file_content = await file.read()
        pdf = PDFQuery(BytesIO(file_content))
        pdf.load()
        text = ''
        text_elements = pdf.pq('LTTextLineHorizontal')
        for t in text_elements:
            text += t.text
        print(text)
