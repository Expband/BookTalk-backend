from fastapi import APIRouter, UploadFile, File, Form
from app.factories import DriverFactory
from app.services import DeeplTranslator
from app.validators import FileContentValidator
from app.handlers import FileHandler

file_handler = FileHandler()
deepl = DeeplTranslator()
driver_factory = DriverFactory()
file_content_validator = FileContentValidator()
router = APIRouter(prefix='/file',
                   tags=['book'],
                   responses={404: {'description': 'Not found'}})


@router.post('/translate')
async def translate_file(file: UploadFile = File(...), target_lang: str = Form(...)):
    await file_handler.read(file)
    translated_text = await file_handler.translate(target_lang)
    return {'translated_text': translated_text}


@router.post('/voice')
async def voice_file(file: UploadFile = File(...), target_lang: str = Form(...)):
    await file_handler.read(file)
    pass
