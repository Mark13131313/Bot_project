import asyncio

from aiogram import Bot, Dispatcher, executor

from config import BOT_TOKEN

loop = asyncio.new_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from handlers import dp, send_hello

    executor.start_polling(dp, on_startup=send_hello)

# File "C:\Users\User\Desktop\Bot_project\main.py", line 12, in <module>
#     from handlers import dp, send_hello
#   File "C:\Users\User\Desktop\Bot_project\handlers.py", line 28, in <module>
#     @dp.callback_query_handlers(text_contains='bunch')
# TypeError: 'Handler' object is not callable


# Control line 12
