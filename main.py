from aiogram import executor
import logging
from config import dp
from handlers import commands, callbacks, extra, admin


commands.register_handlers_commands(dp)
callbacks.register_handlers_callback(dp)
admin.register_handler_admins(dp)

extra.register_extra_handlers(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
