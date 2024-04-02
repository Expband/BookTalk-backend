from .IBaseVAlidator import IBaseValidator
from app.services import DeeplTranslator
from fastapi import HTTPException


class FileContentValidator(IBaseValidator):
    def __init__(self):
        self.deepl = DeeplTranslator()


    async def validate(self, file_text):
        if len(file_text) == 0:
            raise HTTPException(status_code=422, detail='No content provided to process')
        if not await self.deepl.check_if_source_lang_exist(file_text):
            raise HTTPException(status_code=422, detail='No available source language')
