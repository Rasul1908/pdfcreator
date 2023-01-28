import pandas
from fpdf import FPDF

pdf=FPDF(orientation='P',format='a4',unit='mm')

df=pandas.read_csv('topics.csv')


for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Times',style='B',size=24)
    pdf.set_text_color(100,100,254)

    pdf.cell(w=0,h=0,txt=row['Topic'],align='L',ln=1)
    pdf.line(10,20,200,20)



pdf.output('PDFcreated.pdf')