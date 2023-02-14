from aiogram import types

async def set_default_commans(dp):
    await dp.bot.set_mysommands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('help', 'помощь'),
        types.BotCommand('update', 'Апдейт'),
    ])