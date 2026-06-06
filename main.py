import asyncio
from aiogram.types import BotCommand
from bot.bot import bot, dp
from bot.handlers.start import router as start_router


async def main():
    dp.include_router(start_router)

    print("Bot is running")
    await bot.set_my_commands([
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="help", description="Show help message"),
    ])
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())