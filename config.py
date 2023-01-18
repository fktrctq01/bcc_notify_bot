import os
from aiogram.dispatcher import Dispatcher
from aiogram import Bot

CHAT_ID_1 = "188871914"
CHAT_ID_2 = "293108350"

TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# webhook settings
WEBHOOK_HOST = f'https://bcc-notify-bot-service.onrender.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)

# email settings
EMAIL = "bcc_notification@mail.ru"
EMAIL_PWD = os.getenv('EMAIL_PWD')
SMTP_SERVER = "imap.mail.ru"

PATTERN_TEXT = r'Уважаемый\(-ая\), \w+ \w+ \w+! ' \
               r'Сообщаем, что по Вашей карте [\d\*]{16} (?P<trn_time>[\d\.]+) (?P<trn_date>[\d\.]+) ' \
               r'произошло списание на сумму (?P<trn_amount>[\d\.]+) (?P<trn_currency>[a-zA-Z]+)\. ' \
               r'На текущий момент [\d\.]+ [\d\.]+ остаток на Вашей карте [\d\*]{16} ' \
               r'составляет (?P<balance>[\d\.]+) (?P<balance_currency>[a-zA-Z]+)\. (?P<merchant>.+)'

