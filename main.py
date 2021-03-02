from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

from fastapi import FastAPI

app = FastAPI()



parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
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
    return name_crypto, price_rub

  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

  
@app.get('/')
async def get_crypto_price(id:str):
  name, price = await get_price(id)
  return {
    'coin':name,
    'price':price
    }
  
