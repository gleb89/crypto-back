from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

from fastapi import FastAPI

app = FastAPI()

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
async def get_crypto_price(id:str):
  name, price = await get_price(id)
  return {
    'coin':name,
    'price':price
    }

# 1027 - ethereum
# 1 - bitcoin