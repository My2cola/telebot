from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from keybords.default import kb_epic

@dp.message_handler(Command("epic"))
async def epic(message: types.Message):
    await message.answer("Выбери кнопку для просмотра обновления ", reply_markup=kb_epic)