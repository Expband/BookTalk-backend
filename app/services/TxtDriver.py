from fastapi import UploadFile, File
from .IDriver import IDriver


class TxtDriver(IDriver):
    @staticmethod
    async def read(file: UploadFile = File(...)):
        file_content = await file.read()
        print(file_content.decode('utf-8'))
