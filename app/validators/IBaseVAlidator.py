from abc import ABC


class IBaseValidator(ABC):
    async def content_validate(self, content):
        pass

    async def validate_str_length(self, content: str):
        pass

    async def file_extension_validator(self, file):
        pass
