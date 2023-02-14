from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_game = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/hearthstone'),
            KeyboardButton(text='/lol'),
        ],


    ],
    resize_keyboard=True
)