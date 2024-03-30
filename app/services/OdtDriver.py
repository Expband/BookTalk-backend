from .IDriver import IDriver
from io import BytesIO
from odf import text, teletype
from odf.opendocument import load
from fastapi import File, UploadFile


class OdtDriver(IDriver):
    @staticmethod
    async def read(file: UploadFile = File(...)):
        file_content = await file.read()

        # Create a BytesIO object to simulate a file
        file_buffer = BytesIO(file_content)

        # Load the ODT file from the BytesIO object
        doc = load(file_buffer)

        # Extract text content
        text_content = ""
        for para in doc.getElementsByType(text.P):
            text_content += teletype.extractText(para)

        print(text_content)
