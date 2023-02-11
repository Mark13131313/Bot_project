from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from config import URL_Buch_Anfanger, URL_Buch_Experte

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Buch1'),
            KeyboardButton(text='Buch2')
        ],
        [
            KeyboardButton(text='Buch3')
        ]
    ],
    resize_keyboard=True
)

cb = CallbackData('buy', 'id', 'name', 'price')

keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Buch_Anfanger', callback_data='buy:0:buch:250'),
            InlineKeyboardButton(text='Buch_Expert', callback_data='buy:1:buch1:500')
        ],
        [
            InlineKeyboardButton(text='Cancel', callback_data='cancel')
        ]
    ]
)

buch_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Buy', url=URL_Buch_Anfanger)
        ]

    ]
)
buch1_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Buy', url=URL_Buch_Experte)
        ]

    ]
)
