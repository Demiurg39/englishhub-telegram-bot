import os
from dotenv import load_dotenv
from pydantic import SecretStr

load_dotenv()


class Config:
    BOT_TOKEN: SecretStr = SecretStr(os.getenv("BOT_API_KEY"))


config = Config()
