from fastapi import UploadFile, File
from .IDriver import IDriver


class TxtDriver(IDriver):
    @staticmethod
    async def read(file: UploadFile = File(...)):
        file_content = await file.read()
        text = file_content.decode('utf-8')
        return text
