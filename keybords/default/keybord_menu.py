from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/steam'),
            KeyboardButton(text='/epic'),
            KeyboardButton(text='/lesta'),
            KeyboardButton(text='/riot'),
            KeyboardButton(text='/battleNet'),




        ],


    ],
    resize_keyboard=True
)