from app.services import *


class DriverFactory:
    @staticmethod
    async def choose_file_driver(file_extension: str):
        try:
            if file_extension == 'pdf':
                return PdfDriver
            if file_extension == 'docx':
                return DocxDriver
            if file_extension == 'txt':
                return TxtDriver
            if file_extension == 'rtf':
                return RtfDriver
            if file_extension == 'odt':
                return OdtDriver
            if file_extension == 'pptx':
                return PptxDriver
        except Exception as e:
            print(e)
