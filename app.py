async def on_startup(dp):
    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils.set_bot_commands import set_default_commans
    await set_default_commans(dp)

    print('Бот запрущен')


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    executor.start_polling(dp)
