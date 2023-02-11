from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from config import chat_id
from keyboards import keyboard, keyboard1, buch_key, buch1_key
from main import bot, dp


async def send_hello(dp):
    await bot.send_message(chat_id=chat_id, text='Hello')


@dp.message_handler(Command('shop'))
async def show_shop(message: Message):
    await message.answer('Shop', reply_markup=keyboard)


@dp.message_handler(Text(equals=['Buch1', 'Buch2', 'Buch3']))
async def get_goods(message: Message):
    await message.answer(message.txt, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Command('buckshot'))
async def show(message: Message):
    await message.answer(text='Buy or cancel', reply_markup=keyboard1)


@dp.callback_query_handlers(text_contains='bunch')
async def buch(call: CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer('Buy', reply_markup=buch_key)


@dp.callback_query_handlers(text_contains='buch1')
async def buch1(call: CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer('Buy', reply_markup=buch1_key)


@dp.callback_query_handler(text_contains='cancel')
async def cancel(call: CallbackQuery):
    await call.answer('Close', show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)
