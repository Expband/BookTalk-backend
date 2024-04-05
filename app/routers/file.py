from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import StreamingResponse
from app.factories import DriverFactory
from app.services import DeeplTranslator, TtsService, MP3Reader
from app.validators import FileContentValidator, FileValidator
from app.handlers import FileHandler
import io

file_handler = FileHandler()
deepl = DeeplTranslator()
tts = TtsService()
mp_3_reader = MP3Reader()
driver_factory = DriverFactory()
file_content_validator = FileContentValidator()
file_validator = FileValidator()
router = APIRouter(prefix='/file',
                   tags=['book'],
                   responses={404: {'description': 'Not found'}})


@router.post('/translate')
async def translate_file(file: UploadFile = File(...), target_lang: str = Form(...)):
    print(file.filename)
    await file_validator.file_extension_validator(file)
    await file_handler.read(file)
    translated_text = await file_handler.translate(target_lang)
    return {'translated_text': translated_text}


@router.post('/voice')
async def voice_file(file: UploadFile = File(...)):
    await file_validator.file_extension_validator(file)
    await file_handler.read(file)
    file_text = await file_handler.return_file_text()
    if await file_content_validator.validate_str_length(file_text):
        await tts.voice_text(file_text)
        await tts.save_response_to_file()
        mp_3_data = await mp_3_reader.read_mp_3_file(f'../Bucket/{await tts.return_file_name()}.mp3')
        return StreamingResponse(io.BytesIO(mp_3_data), media_type='audio/mpeg',
                                 headers={"Access-Control-Allow-Origin": "*"})
    else:
        raise HTTPException(status_code=400, detail='Length of text more than 4096 symbols ')
