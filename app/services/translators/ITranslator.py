from abc import ABC


class ITranslator(ABC):
    def __init__(self):
        pass

    async def translate(self, text: str, target_lang: str) -> str:
        pass
