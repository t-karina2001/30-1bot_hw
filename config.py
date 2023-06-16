from aiogram import Bot, Dispatcher
from decouple import config


TOKEN = config('TOKEN')
ADMINs = ['426765865', ]
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

