class MP3Reader:

    async def read_mp_3_file(self, path) -> bytes:
        with open(path, 'rb') as file:
            return file.read()
