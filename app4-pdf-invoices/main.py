import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob('Invoices/*.xlsx')
print(filepaths)

for filepath in filepaths:

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, date = filename.split('-')

    pdf.set_font(family='Arial', style='B', size=16)
    pdf.cell(w=50, h=10, txt=f'Invoice nr.{invoice_nr}', align='L', ln=1)

    pdf.set_font(family='Arial', style='B', size=16)
    pdf.cell(w=50, h=10, txt=f'Date: {date}', align='L', ln=1)

    df = pd.read_excel(filepath, sheet_name='Sheet 1')

    # Add a header
    columns_a = list(df.columns)
    columns_a = [item.replace('_', ' ').title() for item in columns_a]
    pdf.set_font(family='Times', style='I', size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns_a[0], border=1)
    pdf.cell(w=70, h=8, txt=columns_a[1], border=1)
    pdf.cell(w=30, h=8, txt=columns_a[2], border=1)
    pdf.cell(w=30, h=8, txt=columns_a[3], border=1)
    pdf.cell(w=30, h=8, txt=columns_a[4], border=1, ln=1)


    # Add rows to the table
    for index, row in df.iterrows():
        pdf.set_font(family='Arial', style='B', size=12)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=70, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, ln=1)

    # Add a total sum
    total_sum = df['total_price'].sum()
    pdf.set_font(family='Arial', style='B', size=12)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)


    # Add a total sum sentence
    pdf.set_font(family='Arial', style='B', size=10)
    pdf.cell(w=30, h=8, txt=f"Total sum is {total_sum}", ln=1)

    # Company name and logo
    pdf.set_font(family='Arial', style='B', size=14)
    pdf.cell(w=30, h=8, txt=f"PythonHow", ln=1)
    pdf.image('pythonhow.png', w=10)

    pdf.output(f'PDFs/{filename}.pdf')
