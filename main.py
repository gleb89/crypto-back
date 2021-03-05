from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from service.service import get_price, get_user_by_email



app = FastAPI()



origins = [
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







@app.get('/')
async def get_crypto_price():
  list_crypto = []
  name_bit, price_bit = await get_price('1')
  name_eth, price_eth = await get_price('1027')
  bitcion =  {
            'coin':name_bit,
            'price':int(price_bit)
            }
  list_crypto.append(bitcion)
  ethereum = {
            'coin':name_eth,
            'price':int(price_eth)
            }
  list_crypto.append(ethereum)
  return list_crypto



@app.post('/crypto')
async def send_data_exc(data:dict):
  return await get_user_by_email(data)





