from .IDriver import IDriver
from fastapi import File, UploadFile
import io
import zipfile
import xml.etree.ElementTree as ET


class PptxDriver(IDriver):
    @staticmethod
    async def read(file: UploadFile = File(...)):
        file_content = await file.read()
        print(file_content)
        file_obj = io.BytesIO(file_content)

        # Open the ZIP archive
        with zipfile.ZipFile(file_obj, "r") as zip_file:
            # Iterate over each file in the archive
            for name in zip_file.namelist():
                if name.startswith("ppt/slides/slide") and name.endswith(".xml"):
                    # Extract text from slide XML
                    with zip_file.open(name) as slide_file:
                        slide_content = slide_file.read()
                        slide_xml = ET.fromstring(slide_content)
                        text = ''
                        for elem in slide_xml.iter():
                            if elem.tag.endswith("t") and elem.text is not None:  # Text element with non-None text
                                text += elem.text + " "
                        print(f"{text}")
