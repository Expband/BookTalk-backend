from .ITranslator import ITranslator
import deepl
import detectlanguage
from fastapi import HTTPException
from app.config import ConfigParser


class DeeplTranslator(ITranslator):
    def __init__(self):
        super().__init__()
        self.__config_parser = ConfigParser()
        self.__translator = deepl.Translator(auth_key=self.__config_parser.return_deepl_api_key())

    async def translate(self, text, target_lang: str) -> str:
        try:
            translated_text = self.__translator.translate_text(text, target_lang=target_lang)
            return translated_text.text
        except:
            raise HTTPException(status_code=503, detail='Translate service currently unavailable')

    async def check_if_source_lang_exist(self, text: str):
        try:
            detectlanguage.configuration.api_key = self.__config_parser.return_detectlang_api_key()
            text_source_lang = detectlanguage.simple_detect(text)
            for language in self.__translator.get_source_languages():
                if str.upper(text_source_lang) in language.code:
                    return True
            return False
        except:
            raise HTTPException(status_code=503, detail='Detect language service currently unavailable')
