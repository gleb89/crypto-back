from fastapi import APIRouter

from service.service import get_user_by_email, get_list_crypto

price_crypto = APIRouter()
email = APIRouter()

@price_crypto.get('/')
async def get_crypto_price():
  return await get_list_crypto()


@email.post('/')
async def send_data_exc(data:dict):
  return await get_user_by_email(data)