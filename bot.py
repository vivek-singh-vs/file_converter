from telegram import Update, inlinekeyboardbutton, inlinekeyboardmarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from pathlib import Path
from PIL import Image
import fitz
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

DOWNLOAD_DIR = Path("downloads")
OUTPUT_DIR = Path("outputs")
DOWNLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)


# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I’m your bot. How can I help you today?")

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Available commands:\n/start - Welcome message\n/help - Show help")

# Echo handler
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)


async def file_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message.photo:
        file = await message.photo[-1].get_file()
        input_path = DOWNLOAD_DIR / f"{file.file_id}.jpg"
        output_path = OUTPUT_DIR / f"{file.file_id}.pdf"
        await file.download_to_drive(input_path)
        image = Image.open(input_path)
        output_pdf = image.convert("RGB")
        output_pdf.save(output_path)
        await message.reply_document(document=output_path)



def main():
    # Create the application
    app = Application.builder().token(TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.add_handler(MessageHandler(filters.PHOTO, file_handler))

    # Run the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
