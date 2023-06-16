from aiogram import Dispatcher, types
from config import bot


async def echo(message: types.Message) -> None:
    if message.text.isdigit():
        squared = int(message.text) ** 2
        await bot.send_message(message.chat.id, f'Квадрат числа {message.text} равен {squared}')
    else:
        await bot.send_message(message.chat.id, message.text)


async def echo_text(message: types.Message) -> None:
    await bot.send_message(message.chat.id, message.text)


def register_extra_handlers(dp: Dispatcher):
    dp.register_message_handler(echo)
    dp.register_message_handler(echo_text, commands='text')
