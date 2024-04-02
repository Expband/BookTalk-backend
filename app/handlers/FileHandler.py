from app.factories import DriverFactory
from app.services import DeeplTranslator
from app.validators import FileContentValidator, FileValidator


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
        await self.__file_validator.validate(self.__file_extension)
        driver = await self.__driver_factory.choose_file_driver(self.__file_extension)
        self.__file_text = await driver.read(file)


    async def translate(self, target_lang: str = '') -> str:
        await self.__file_content_validator.validate(self.__file_text)
        translated_text = await self.__deepl.translate(self.__file_text, target_lang)
        return translated_text

    async def return_file_text(self):
        return self.__file_text
