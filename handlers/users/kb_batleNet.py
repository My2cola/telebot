from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from keybords.default import kb_battleNet

@dp.message_handler(Command("battleNet"))
async def battleNet(message: types.Message):
    await message.answer("Выбери кнопку для просмотра обновления ", reply_markup=kb_battleNet)