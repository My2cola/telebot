from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_epic = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/among_us'),
            KeyboardButton(text='/fall_guys'),
            KeyboardButton(text='/fortnite'),
            KeyboardButton(text='/genshin'),
            KeyboardButton(text='/back_launcher'),
        ],


    ],
    resize_keyboard=True
)