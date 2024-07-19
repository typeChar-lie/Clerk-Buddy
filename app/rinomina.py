import PyPDF2
import os
def extract(pdf_file: str) -> str:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        pdf_text=[]
        for page in reader.pages:
            pdf_text+=page.extract_text()

            return pdf_text
def main(rinomina_PERCORSO_CARTELLA:str):
    cartella = rinomina_PERCORSO_CARTELLA
    with os.scandir(cartella) as entries:
        for entry in entries:
            old_name= cartella + entry.name
            extracted_text= extract(old_name)
            if(extracted_text[1]=='-'):
                numero = '0' + extracted_text[0]
            elif(extracted_text[2]=='-'):
                numero = extracted_text[0] + extracted_text[1]
            else:
                numero = extracted_text[0] + extracted_text[1] + extracted_text[2]
            new_name= cartella + numero + " " + entry.name
            os.rename(old_name, new_name)