import asyncio
import logging
import os
import sys

from telegram.ext import Application, CommandHandler
from config import TELEGRAM_TOKEN, OUTPUT_DIR
from orchestrator import run_thesis_pipeline

# ====== FORCE UTF-8 ======
os.environ["PYTHONIOENCODING"] = "utf-8"
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# ====== LOGGING SAFE ======
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ====== COMMANDS ======
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
            safe_text = text.encode("utf-8", errors="ignore").decode("utf-8")
            await msg.edit_text(safe_text)
        except Exception as e:
            logging.warning(f"edit_text failed: {e}")

    try:
        result = await run_thesis_pipeline(topic, cb)

        with open(result["pdf_path"], "rb") as f:
            await context.bot.send_document(
                chat_id=update.effective_chat.id,
                document=f
            )

    except Exception as e:
        await update.message.reply_text(str(e))

# ====== MAIN ======
def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("generate", generate))

    app.run_polling()

if __name__ == "__main__":
    main()
