from app.factories import DriverFactory
from app.services import DeeplTranslator
from app.validators import FileContentValidator, FileValidator
from fastapi import HTTPException


class FileHandler:
    def __init__(self):
        self.__deepl = DeeplTranslator()
        self.__driver_factory = DriverFactory()
        self.__file_content_validator = FileContentValidator()
        self.__file_validator = FileValidator()
        self.__file_extension = str
        self.__file_text = str

    async def read(self, file):
        self.__file_extension = file.filename.split('.')[-1]
        driver = await self.__driver_factory.choose_file_driver(self.__file_extension)
        try:
            self.__file_text = await driver.read(file)
        except:
            raise HTTPException(status_code=422, detail='Unable to process file content')



    async def translate(self, target_lang: str = '') -> str:
        await self.__file_content_validator.content_validate(self.__file_text)
        translated_text = await self.__deepl.translate(self.__file_text, target_lang)
        return translated_text

    async def return_file_text(self):
        return self.__file_text
