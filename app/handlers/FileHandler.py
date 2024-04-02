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



    async def translate(self, file, target_lang: str = ''):
        self.__file_extension = file.filename.split('.')[-1]
        await self.__file_validator.validate(self.__file_extension)
        driver = await self.__driver_factory.choose_file_driver(self.__file_extension)
        file_text = await driver.read(file)
        await self.__file_content_validator.validate(file_text)
        translated_text = await self.__deepl.translate(file_text, target_lang)
        return translated_text
