from gemini_client import safe_generate

class ResearcherAgent:
    def __init__(self, api_key):
        pass

    def gather(self, topic):
        return {"summary": safe_generate("معلومات أكاديمية عن: " + topic)}
