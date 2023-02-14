from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from keybords.default import kb_riot

@dp.message_handler(Command("riot"))
async def riot(message: types.Message):
    await message.answer("Выбери кнопку для просмотра обновления ", reply_markup=kb_riot)