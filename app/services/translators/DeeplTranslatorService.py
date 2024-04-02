from .ITranslator import ITranslator
import deepl
import detectlanguage


class DeeplTranslator(ITranslator):
    def __init__(self):
        super().__init__()
        self.__translator = deepl.Translator(auth_key='9c4b0dc9-8236-414b-8ce6-450f06d9622c:fx')

    async def translate(self, text: str, target_lang: str) -> str:
        translated_text = self.__translator.translate_text(text, target_lang=target_lang)
        return translated_text.text

    async def check_if_source_lang_exist(self, text: str):
        detectlanguage.configuration.api_key = '194f8dc31ce4bf0b1460ece885aad7ba'
        text_source_lang = detectlanguage.simple_detect(text)
        for language in self.__translator.get_source_languages():
            if str.upper(text_source_lang) in language.code:
                return True
        return False
