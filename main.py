from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P",unit="mm",format="A4")
df=pd.read_csv("content.csv")
for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_auto_page_break(False)
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt=row["topic"],align="C")
    for line in range(20,250,10):
        pdf.line(10,line,200,line)
    # pdf.ln(260)
    # pdf.cell(0,10,txt=row["topic"],align="R")
    pages=int(row["pages"])-1
    for page in range(pages):
        pdf.add_page()
        for line in range(20, 250, 10):
            pdf.line(10, line, 200, line)
        pdf.set_font("Arial",size=12)

pdf.output("outbput.pdf","F")