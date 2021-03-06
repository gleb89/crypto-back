from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import string
import smtplib

from config.config import Config

config = Config

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.api_key,
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


async def get_list_crypto():
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


async def get_user_by_email(data):
    alphabet = string.ascii_letters + string.digits
    servece = data['operation']
    coin = data['crypto']
    sum_coin = data['count_crypto']
    rub_coin = data['count_rub']
    
    if servece == 'Покупка':
      adrr = data['numberadres']
    if servece == 'Продажа':
      adrr = data['numbercard']
    message_for_client = f'Здравствуйте уважаемый клиент!\n \
                        ваш обмен:{servece} {coin},\n \
                        на сумму:{sum_coin} coin -  {rub_coin} руб.\n \
                        будет совершен в ближайшее время!\n \
                        C уважением Speed-crypto'.encode('utf-8')

    message_for_me = f'Заказан обмен:{servece} {coin},\n \
                        на сумму:{sum_coin} - {rub_coin} руб\n \
                        адрес = {adrr}\n \
                        C уважением Speed-crypto'.encode('utf-8')

    server = smtplib.SMTP('smtp.mail.ru',587)
    server.starttls()
    server.login(config.login_email,config.password_email)
    server.sendmail(config.login_email, data['email'] , message_for_client)
    server.sendmail(config.login_email, config.login_email,  message_for_me)
    server.close()
    try:
      return {'message':'ок'}
    except:
      return {'message':'false'}