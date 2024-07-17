from PyPDF2 import PdfReader, PdfWriter, PaperSize
import os
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Estrazione Testo PDF
def extract(pdf_file: str) -> str:
    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf, strict=False)
        pdf_text=[]
        for page in reader.pages:
            pdf_text+=page.extract_text()

            return pdf_text
# Timbro
def timbra_pagate(fatturaPath:str, fatturaNum:int, timbro_PERCORSO_NUMERO:str, timbro_PERCORSO_METODO:str):
    nTimbri=0
    ultimoMetodo=""
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)
    can.setFontSize(24)
    numeri = enumerate(open(timbro_PERCORSO_NUMERO, 'r').readlines())
    metodi= open(timbro_PERCORSO_METODO, 'r').readlines()
    for i, numero in numeri:
        if(numero.strip()==fatturaNum):
            metodo = metodi[i].strip()
            if(nTimbri==0):
                can.drawString(35, 780, 'PAGATO')
                can.drawString(35, 755, metodo)
                ultimoMetodo = metodo
            elif(nTimbri==1):
                if(ultimoMetodo!=metodo):
                    can.drawString(35, 730, metodo)
                    ultimoMetodo = metodo
            elif(nTimbri==2):
                if(ultimoMetodo!=metodo):
                    can.drawString(35, 705, metodo)
            nTimbri += 1
        elif(nTimbri>0):
            break       
    
    can.save()

    timbro= PdfReader(packet).pages[0]
    fattura = PdfReader(open(fatturaPath,'rb'))
    output = PdfWriter()
    width = PaperSize.A4.width
    height = PaperSize.A4.height

    fattura.pages[0].merge_page(timbro)
    
    for i in range(0, len(fattura.pages)):
        page = fattura.pages[i]
        page.scale_to(width, height)
        output.add_page(page)

    output_pdf = open(fatturaPath, 'wb')
    output.write(output_pdf)
    output_pdf.close()
# Esecuzione
def main(timbro_PERCORSO_CARTELLA:str, timbro_PERCORSO_NUMERO:str, timbro_PERCORSO_METODO:str):
    cartella = timbro_PERCORSO_CARTELLA
    with os.scandir(cartella) as fatture:
        for fattura in fatture:
            nome_file= cartella + fattura.name
            extracted_text= extract(nome_file)
            if(extracted_text[1]=='-'):
                num = extracted_text[0]
            elif(extracted_text[2]=='-'):
                num = extracted_text[0] + extracted_text[1]
            else:
                num = extracted_text[0] + extracted_text[1] + extracted_text[2]
            
            timbra_pagate(fattura, num, timbro_PERCORSO_NUMERO, timbro_PERCORSO_METODO)