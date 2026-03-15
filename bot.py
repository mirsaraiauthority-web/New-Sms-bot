import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8680439397:AAH6cSffENVvr9BRb2FEHnCGz2OL_8y2k-Y"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is working!")

async def sms(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:
        number = context.args[0]
        message = " ".join(context.args[1:])

        api = f"http://hakvolution.com/KEY/sub.php?key=&number=&msg=}"

        requests.get(api)

        await update.message.reply_text("SMS Sent!")

    except:
        await update.message.reply_text("Usage:\n/sms 017XXXXXXXX Hello")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sms", sms))

app.run_polling()
