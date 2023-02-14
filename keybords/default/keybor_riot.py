from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_riot = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/lol'),
            KeyboardButton(text='/valorant'),
            KeyboardButton(text='/back_launcher'),
        ],


    ],
    resize_keyboard=True
)