from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from keybords.default import kb_menu

@dp.message_handler(Command("back_launcher"))
async def back_launcher(message: types.Message):
    await message.answer("Выбери лаучер игры ", reply_markup=kb_menu)
