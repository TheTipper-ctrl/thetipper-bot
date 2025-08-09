
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to TheTipper_Bot! ⚽️\nType /predict to get started.")

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔮 Prediction feature coming soon...")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("predict", predict))
    app.run_polling()

if __name__ == "__main__":
    main()
