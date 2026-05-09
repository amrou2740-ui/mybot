import json
import os
from config import GEMINI_API_KEY, OUTPUT_DIR
from agents.strategist import StrategistAgent
from agents.researcher import ResearcherAgent
from agents.writer import WriterAgent
from agents.data_viz import DataVizAgent
from agents.compiler import CompilerAgent

os.makedirs(OUTPUT_DIR, exist_ok=True)

async def run_thesis_pipeline(topic, cb=None):

    async def update(msg):
        if cb:
            await cb(msg)
        print(msg)

    await update("بدء التحليل...")

    strategist = StrategistAgent()
    outline_raw = strategist.create_outline(topic)

    try:
        outline = json.loads(outline_raw)
    except:
        outline = {"chapters":[{"title":"مقدمة"},{"title":"خاتمة"}]}

    await update("جمع المعلومات...")

    researcher = ResearcherAgent(GEMINI_API_KEY)
    data = researcher.gather(topic)

    writer = WriterAgent(GEMINI_API_KEY)

    chapters = {}

    for c in outline["chapters"]:
        chapters[c["title"]] = writer.write(c["title"], data["summary"])

    await update("إنشاء الرسوم...")

    viz = DataVizAgent()
    imgs = viz.make(topic, OUTPUT_DIR)

    await update("تجميع PDF...")

    comp = CompilerAgent()
    pdf = comp.build(chapters, imgs, OUTPUT_DIR)

    await update("انتهى")

    return {"pdf_path": pdf}
