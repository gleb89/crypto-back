from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '115640cb-4181-4cdb-b65c-f9291338de8f',
}

session = Session()
session.headers.update(headers)

async def get_price(id):
  url_price = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id={id}'
  try:
    response = session.get(url_price )
    data = json.loads(response.text)
    name_crypto = data['data'][id]['name']

    price_usd = data['data'][id]['quote']['USD']['price']
    price_rub = price_usd * 76
    staff = price_rub/ 100 * 10
    price = price_rub + staff
    return name_crypto, price

  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


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
