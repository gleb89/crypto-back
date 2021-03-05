import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    login_email = os.getenv('LOGIN_EMAIL')
    password_email = os.getenv('PASSWORD_EMAIL')
    api_key = os.getenv('API_KEY_COIN')