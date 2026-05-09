from gemini_client import safe_generate

class StrategistAgent:
    def create_outline(self, topic):
        prompt = "أنشئ خطة أكاديمية بصيغة JSON للموضوع: " + topic
        return safe_generate(prompt)
