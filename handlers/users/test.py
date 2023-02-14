from aiogram import types
from loader import dp
from keybords.default import kb_test

@dp.message_handler(text='/любой тект')
async def test(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}! \n'
                         f'тут должен быть какойто текст', reply_markup=kb_test)