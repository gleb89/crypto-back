from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from routers.routers import email, price_crypto
from fastapi.responses import HTMLResponse


app = FastAPI()



origins = [
    "https://speedcrypto.ru",
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",


]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)







app.include_router(
    price_crypto,
    prefix="/crypto",
    tags=["crypto"],
    responses={404: {"description": "Not found"}})


app.include_router(
    email,
    prefix="/email",
    tags=["email"],
    responses={404: {"description": "Not found"}})


@app.post('/')
def home():

  return {'kkk':'hhh'}
