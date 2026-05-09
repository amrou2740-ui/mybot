import asyncio
import logging
import os
from telegram.ext import Application, CommandHandler
from config import TELEGRAM_TOKEN, OUTPUT_DIR
from orchestrator import run_thesis_pipeline

logging.basicConfig(level=logging.INFO)
os.makedirs(OUTPUT_DIR, exist_ok=True)

async def start(update, context):
    await update.message.reply_text("أرسل /generate + الموضوع")

async def generate(update, context):
    if not context.args:
        await update.message.reply_text("اكتب موضوع")
        return

    topic = " ".join(context.args)
    msg = await update.message.reply_text("جاري المعالجة...")

    async def cb(text):
        try:
            await msg.edit_text(text)
        except:
            pass

    try:
        result = await run_thesis_pipeline(topic, cb)
        await context.bot.send_document(update.effective_chat.id, open(result["pdf_path"], "rb"))
    except Exception as e:
        await update.message.reply_text(str(e))

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("generate", generate))
    app.run_polling()

if __name__ == "__main__":
    main()
