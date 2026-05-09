from gemini_client import safe_generate

class WriterAgent:
    def __init__(self, api_key):
        pass

    def write(self, title, context):
        return safe_generate(title + "\n" + context)
