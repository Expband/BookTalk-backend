from .IBaseVAlidator import IBaseValidator
from fastapi import HTTPException


class FileValidator(IBaseValidator):
    async def file_extension_validator(self, file):
        try:
            file_extension = file.filename.split('.')[-1]
        except Exception as ex:
            raise HTTPException(status_code=422, detail='No file extension')
        available_extensions = ['docx', 'pdf', 'txt', 'rtf', 'odt', 'pptx']
        if file_extension not in available_extensions:
            raise HTTPException(status_code=422, detail='Unprocessable file extension')
