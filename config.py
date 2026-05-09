import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "PUT_YOUR_TOKEN_HERE")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "PUT_YOUR_KEY_HERE")

# أقوى موديل مستقر
GEMINI_MODEL = "gemini-2.5-flash"

OUTPUT_DIR = "output"
