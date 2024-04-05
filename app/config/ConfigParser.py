from dotenv import load_dotenv
import os


class ConfigParser:
    def __init__(self):
        load_dotenv()
        self.__DEPL = os.getenv('DEPL')
        self.__DETECTLANG = os.getenv('DETECTLANGUAGE')
        self.__OPENAI = os.getenv('OPENAI')

    def return_deepl_api_key(self):
        return self.__DEPL

    def return_detectlang_api_key(self):
        return self.__DETECTLANG

    def return_open_ai_api_key(self):
        return self.__OPENAI
