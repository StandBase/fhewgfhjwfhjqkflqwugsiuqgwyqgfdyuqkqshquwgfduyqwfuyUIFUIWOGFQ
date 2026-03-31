from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8680410776:AAHg_WutRFYcUzrXCZ6mNuZnYoFlfbJn1yo"

async def dwd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("привет")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("dwd", dwd))

print("Бот запущен...")
app.run_polling()
