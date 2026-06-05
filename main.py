import asyncio

from bot.bot import bot, dp
from bot.handlers.start import router as start_router


async def main():
    dp.include_router(start_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())