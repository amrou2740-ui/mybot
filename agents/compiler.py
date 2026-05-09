from fpdf import FPDF
import os

class CompilerAgent:
    def build(self, chapters, images, output_dir):
        pdf = FPDF()
        pdf.add_page()

        for t,c in chapters.items():
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0,10,t+"\n"+c)

        for img in images:
            pdf.add_page()
            pdf.image(img,w=180)

        path = os.path.join(output_dir,"thesis.pdf")
        pdf.output(path)
        return path
