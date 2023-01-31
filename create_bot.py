from pyqiwip2p import AioQiwiP2P
from aiogram import Bot
from aiogram.dispatcher import Dispatcher

bot = Bot(token='5938946714:AAHAp-YIuOiPSXr4VMfxPheLG51Y3BFtKJc')
dp = Dispatcher(bot)

QIWI_PRIV_KEY = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6IjR1OGl1MS0wMCIsInVzZXJfaWQiOiI3OTk5MTY0NTAyOCIsInNlY3JldCI6IjBmZjFiZGI0OTI0NmE0MDgyMjk2YTZmYjg4MDZiMGEyOGZlNWFkZWZmZDA2MTg4MDdjOTdhMzY2YmIxYWIxZDAifX0="

p2p = AioQiwiP2P(auth_key=QIWI_PRIV_KEY)