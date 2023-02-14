from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from keybords.default import kb_steam

@dp.message_handler(Command("steam"))
async def steam(message: types.Message):
    await message.answer("Выбери кнопку для просмотра ", reply_markup=kb_steam)