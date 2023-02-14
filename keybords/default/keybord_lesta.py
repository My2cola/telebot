from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_lesta = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='?'),
            KeyboardButton(text='/back_launcher'),
        ],


    ],
    resize_keyboard=True
)