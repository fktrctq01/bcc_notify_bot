import os
from aiogram.dispatcher import Dispatcher
from aiogram import Bot

TOKEN = "5809115649:AAFY_VbsgGe7RvCZA2Fu12-KnaEG-8W1e4E"
# os.getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# webhook settings
WEBHOOK_HOST = f'https://bcc-notify-bot-service.onrender.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)
