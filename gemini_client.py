import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(GEMINI_MODEL)

def safe_generate(prompt, retries=3):
    for i in range(retries):
        try:
            return model.generate_content(prompt).text
        except Exception as e:
            if i == retries - 1:
                return "خطأ في الاتصال بالنموذج"
