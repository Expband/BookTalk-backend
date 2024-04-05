from openai import OpenAI
from app.config import ConfigParser
import uuid


class TtsService:
    def __init__(self):
        self.__config_parser = ConfigParser()
        self.__client = OpenAI(api_key=self.__config_parser.return_open_ai_api_key())
        self.__response = None
        self.__file_name = str

    async def voice_text(self, text: str):
        self.__response = self.__client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text,
        )

    async def save_response_to_file(self):
        self.__file_name = str(uuid.uuid4())
        self.__response.write_to_file(f'../Bucket/{self.__file_name}.mp3')

    async def return_file_name(self):
        return self.__file_name
