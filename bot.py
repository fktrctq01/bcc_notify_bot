import asyncio
import logging

from aiogram import types, Dispatcher
from aiogram.utils.exceptions import BotBlocked
from aiogram.utils.executor import start_webhook

import messages
from clients.emailc import connect, get_all_unseen_mail, close
from config import bot, dp, WEBHOOK_PATH, WEBAPP_HOST, WEBHOOK_URL, CHAT_ID_1, CHAT_ID_2


async def on_startup(dispatcher: Dispatcher) -> None:
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)
    asyncio.create_task(background_on_start())


async def background_on_start() -> None:
    while True:
        try:
            try:
                logging.info("Проверяем почту")
                imap = connect()
                for message in get_all_unseen_mail(imap):
                    await bot.send_message(CHAT_ID_1, text=message, disable_web_page_preview=True)
                    await bot.send_message(CHAT_ID_2, text=message, disable_web_page_preview=True)
                close(imap)
            except TypeError as e:
                logging.error(e)
                await bot.send_message(CHAT_ID_1, text=e)
        except BotBlocked:
            logging.error("Бот остановлен или заблокирован")
        await asyncio.sleep(30)


async def on_shutdown(dispatcher: Dispatcher) -> None:
    await bot.delete_webhook()


@dp.message_handler(commands=['start', 'hello'])
async def send_welcome(message: types.Message):
    await message.answer(messages.WELCOME_MESSAGE)


@dp.message_handler(commands=['report'])
async def generate_report(message: types.Message):
    pass


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
