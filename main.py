import pandas
from fpdf import FPDF

pdf=FPDF(orientation='P',format='a4',unit='mm')
pdf.set_auto_page_break(auto=False,margin=0)

df=pandas.read_csv('topics.csv')


for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Times',style='B',size=24)
    pdf.set_text_color(100,100,254)

    pdf.cell(w=0,h=0,txt=row['Topic'],align='L',ln=1)


    pdf.ln(265)
    pdf.set_font(family='Times',style='I',size=8)
    pdf.set_text_color(150,150,150)
    pdf.cell(w=0,h=12,txt=row['Topic'],align='R')

    for y in range(15,265,10):
        pdf.line(10,y,200,y)


    for i in range(row['Pages']-1):
        pdf.add_page()
        pdf.ln(265)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(150, 150, 150)
        pdf.cell(w=0, h=12, txt=row['Topic'], align='R')

        for y in range(15, 265, 10):
            pdf.line(10, y, 200, y)

pdf.output('PDFcreated.pdf')


