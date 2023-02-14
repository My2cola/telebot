from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from keybords.default import kb_lesta

@dp.message_handler(Command("lesta"))
async def lesta(message: types.Message):
    await message.answer("Выбери кнопку для просмотра обновления ", reply_markup=kb_lesta)