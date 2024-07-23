from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)


df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Arial", style='B', size=22)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L")
    pdf.line(10, 20, 200, 20)
    for i in range(26):
        y1 = 10 * (i + 3)
        y2 = 10 * (i + 3)
        pdf.line(10, y1, 200, y2)

    

    # Add footer
    pdf.ln(270)
    pdf.set_font(family="Arial", style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # Add pages based on the number of pages in the csv
    for i in range(row['Pages'] - 1):
        pdf.add_page()
        pdf.ln(270)
        pdf.set_font(family="Arial", style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        for i in range(28):
            y1 = 10 * (i + 1)
            y2 = 10 * (i + 1)
            pdf.line(10, y1, 200, y2)
            

pdf.output("output.pdf")
