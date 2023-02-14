import requests
from bs4 import BeautifulSoup
import aiogram.types
from aiogram import executor, Dispatcher
from loader import dp, bot
import asyncio
import datetime

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
                text=f'New update for warface: {last_update}',
            )
        await asyncio.sleep(600)

async def update():
    url = "https://валорант.рф/patch/"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        elements = soup.find_all("p", class_="post-date")

        latest_update = None

    for element in elements:
        date_string = element.text
        date_object = datetime.datetime.strptime(date_string, '\n%d.%m.%Y\n')
        if latest_update is None or date_object > latest_update:
            latest_update = date_object

        print("Latest Update Valorant:", latest_update.strftime("%d %B %Y"))
    else:
        print(f"Request failed with status code: {response.status_code}")
        return latest_update

@dp.message_handler(commands='valorant')
async def cmd_send_valorant(message: aiogram.types.Message):
    last_update = await update()
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'last update for valorant: {last_update}',
    )
    asyncio.create_task(check_for_updates(message))


if __name__ == '__main__':
    import logging

    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)