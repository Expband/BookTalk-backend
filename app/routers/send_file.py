from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.factories import DriverFactory

driver_factory = DriverFactory()
router = APIRouter(prefix='/file',
                   tags=['book'],
                   responses={404: {'description': 'Not found'}})


@router.post('/upload')
async def upload_file(file: UploadFile = File(...), target_lang: str = Form(...)):
    file_extension = file.filename.split('.')[-1]
    available_extensions = ['docx', 'pdf', 'txt', 'rtf', 'odt', 'pptx']
    if file_extension not in available_extensions:
        raise HTTPException(status_code=422, detail='Unprocessable file extension')
    driver = await driver_factory.choose_file_driver(file_extension)
    file_text = await driver.read(file)
    print(file_text)
    if len(file_text) == 0:
        raise HTTPException(status_code=422, detail='No content provided to process')
    return {'file_name': f'{str(file.filename)}'}

