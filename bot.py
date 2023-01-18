import asyncio
import logging

from aiogram import types, Dispatcher
from aiogram.types import message
from aiogram.utils.executor import start_webhook

import messages
from clients.emailc import connect, get_all_unseen_mail, close
from config import bot, dp, WEBHOOK_PATH, WEBAPP_HOST, WEBHOOK_URL


async def on_startup(dispatcher: Dispatcher) -> None:
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)
    asyncio.create_task(background_on_start())


async def background_on_start() -> None:
    while True:
        await asyncio.sleep(60)
        logging.INFO("Hello World1")
        print("Hello World1")
        imap = connect()
        lst = get_all_unseen_mail(imap)
        logging.INFO(*lst)
        close(imap)
        print("Hello World2")
        logging.INFO("Hello World2")


async def on_shutdown(dispatcher: Dispatcher) -> None:
    await bot.delete_webhook()


@dp.message_handler(commands=['start', 'hello'])
async def send_welcome(message: types.Message):
    await message.answer(messages.WELCOME_MESSAGE)


@dp.message_handler(commands=['report'])
async def generate_report(message: types.Message):
    await message.answer("Тут будет отчет")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(messages.COMMAND_NOT_RECOGNIZED)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST
    )
