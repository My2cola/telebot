from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_steam = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/steam_game'),
            KeyboardButton(text='/warzon'),
            KeyboardButton(text='/apex'),
            KeyboardButton(text='/warface'),
            KeyboardButton(text='/back_launcher'),
        ],


    ],
    resize_keyboard=True
)