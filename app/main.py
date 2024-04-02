from fastapi import FastAPI
import uvicorn
from routers import file

app = FastAPI()
app.include_router(file.router)

if __name__ == '__main__':
    uvicorn.run(app)
