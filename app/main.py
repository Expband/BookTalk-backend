from fastapi import FastAPI
import uvicorn
from routers import file
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) Configuration
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:5000",
    "http://127.0.0.1:8000",
    # Add any other origins that your frontend might be served from
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"],
)
app.include_router(file.router)

if __name__ == '__main__':
    uvicorn.run(app)
