import logging
from aiogram.utils.executor import start_webhook
from aiogram import types

import messages
from random import choice
from config import bot, dp, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_URL


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


# @dp.message_handler(commands=['start', 'hello'])
# async def send_welcome(message):
#     await message.answer("asd")
#
#
# @dp.message_handler(commands=['report'])
# async def generate_report(message):
#     await message.answer("тут будет отчет")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
