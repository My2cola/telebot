import requests
from bs4 import BeautifulSoup
import aiogram.types
from aiogram import executor, Dispatcher
from loader import dp, bot
import asyncio

async def get_chat_id(update_command: aiogram.types.Message):
    return update_command.chat.id

async def check_for_updates(update_command: aiogram.types.Message):
    chat_id = await get_chat_id(update_command)
    last_update = await update()
    while True:
        new_update = await update()
        if new_update != last_update:
            last_update = new_update
            await bot.send_message(
                chat_id=chat_id,
                text=f'New update for apex: {last_update}',
            )
        await asyncio.sleep(600)



async def update():
    url = "https://www.playground.ru/apex_legends/news/updates"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    last_update = soup.find("time").text
    print("last updates apex: ", last_update)
    return last_update



@dp.message_handler(commands='apex')
async def cmd_send_apex(message: aiogram.types.Message):
    last_update = await update()
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'last update for apex: {last_update}',
    )
    asyncio.create_task(check_for_updates(message))

if __name__ == '__main__':
    import logging

    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
