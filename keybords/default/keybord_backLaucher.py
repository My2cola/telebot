from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/lol'),
            KeyboardButton(text='/valorant'),
        ],


    ],
    resize_keyboard=True
)