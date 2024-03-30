from abc import ABC
from fastapi import File, UploadFile


class IDriver(ABC):
    @staticmethod
    async def read(file: UploadFile = File(...)):
        pass
