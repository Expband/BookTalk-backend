from fastapi import UploadFile, File
from .IDriver import IDriver
from striprtf.striprtf import rtf_to_text


class RtfDriver(IDriver):
    @staticmethod
    async def read(file: UploadFile = File(...)):
        file_content = await file.read()
        rtf = rtf_to_text(file_content.decode('utf-8'))
        print(rtf)
