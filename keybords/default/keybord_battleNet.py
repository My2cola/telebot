from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_battleNet = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/hearthstone'),
            KeyboardButton(text='/back_launcher'),

        ],


    ],
    resize_keyboard=True
)