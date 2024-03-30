from fastapi import APIRouter, UploadFile, File, Form
from app.services import PdfDriver, DocxDriver, PptxDriver, TxtDriver, RtfDriver, OdtDriver


pdf = PdfDriver()
docx = DocxDriver()
pptx = PptxDriver()
txt = TxtDriver()
rtf = RtfDriver()
odt = OdtDriver()
router = APIRouter(prefix='/file',
                   tags=['book'],
                   responses={404: {'description': 'Not found'}})



@router.get('/')
async def return_hello():
    return {'book': 'returned'}


@router.post('/upload')
async def upload_file(file: UploadFile = File(...), target_lang: str = Form(...)):
    await odt.read(file)

    return {'file_name': f'{str(file.filename)}'}
