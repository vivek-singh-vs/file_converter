from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message,BotCommand

router = Router()


@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Bot is running!")

@router.message(Command("help"))
async def help_command(message: Message):
    text = (
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
    )
    await message.answer(text) 