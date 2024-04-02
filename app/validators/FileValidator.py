from .IBaseVAlidator import IBaseValidator
from fastapi import HTTPException


class FileValidator(IBaseValidator):
    async def validate(self, file_extension):
        available_extensions = ['docx', 'pdf', 'txt', 'rtf', 'odt', 'pptx']
        if file_extension not in available_extensions:
            raise HTTPException(status_code=422, detail='Unprocessable file extension')
