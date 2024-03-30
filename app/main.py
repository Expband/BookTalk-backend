from fastapi import FastAPI
import uvicorn
from routers import send_file

app = FastAPI()
app.include_router(send_file.router)

if __name__ == '__main__':
    uvicorn.run(app)
