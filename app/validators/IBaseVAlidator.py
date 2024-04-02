from abc import ABC


class IBaseValidator(ABC):
    async def validate(self, content):
        pass
