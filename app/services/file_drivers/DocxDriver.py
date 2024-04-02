import io
import zipfile
import xml.etree.ElementTree as ET
from fastapi import File, UploadFile, HTTPException
from .IDriver import IDriver


class DocxDriver(IDriver):
    @staticmethod
    async def read(file: UploadFile = File(...)):
        file_content = await file.read()
        file_obj = io.BytesIO(file_content)

        # Open the ZIP archive
        with zipfile.ZipFile(file_obj, "r") as zip_file:
            # Read the content of document.xml
            document_xml_content = zip_file.read('word/document.xml').decode('utf-8')

        # Parse the XML content
        root = ET.fromstring(document_xml_content)

        # Define a function to recursively extract text from elements
        def extract_text(element):
            text = ''
            if element.tag.endswith('t'):
                # If the element is <w:t>, extract its text content
                text += element.text or ''
            for child in element:
                text += extract_text(child)
            return text

        # Extract text from all <w:t> elements in the document
        all_text = extract_text(root)
        return all_text
