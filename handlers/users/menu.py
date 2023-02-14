from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from keybords.default import kb_menu

@dp.message_handler(Command("menu"))
async def menu(message: types.Message):
    await message.answer("выбери лаунчер", reply_markup=kb_menu)
