from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import timbro, rinomina, metodo
from onefileImages import *
from PyPDF2 import PdfReader, PdfWriter, PaperSize
import os
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
# Global variables      // non ho trovato altro modo per farlo funzionare
rinomina_PERCORSO_CARTELLA = ""
metodo_PERCORSO_ELENCO = ""
timbro_PERCORSO_CARTELLA = ""
timbro_PERCORSO_METODO = ""
timbro_PERCORSO_NUMERO = ""
# Functions
## Menu
def menu():
    if(frameMenu.winfo_viewable()):
        if(menu_choice.get() == "rinomina"):
            frameRinomina.place(x=0, y=0, width=645, height=215)  
        elif(menu_choice.get() == "metodo"):
            frameMetodo.place(x=0, y=0, width=645, height=215)
        elif(menu_choice.get() == "timbro"):
            frameTimbro.place(x=0, y=0, width=645, height=215)
        frameMenu.place_forget()
    else:
        frameRinomina.place_forget()
        frameMetodo.place_forget()
        frameTimbro.place_forget()
        frameMenu.place(x=40, y=10, width=130, height=85)

## Rinomina
def btnRinominaCartellaOnClick():
    global rinomina_PERCORSO_CARTELLA
    rinomina_PERCORSO_CARTELLA = filedialog.askdirectory(initialdir="./", title="Scegli cartella PDF") + "/"
    LblCartellaRinomina.config(text = rinomina_PERCORSO_CARTELLA)
    print(rinomina_PERCORSO_CARTELLA)
def btnRinominaEseguiOnClick():
    try:
        global rinomina_PERCORSO_CARTELLA
        if(messagebox.askokcancel(message="Procedere?")):
            print(rinomina_PERCORSO_CARTELLA)
            rinomina.main(rinomina_PERCORSO_CARTELLA)
    except:
        messagebox.Message(message= "Selezionare percorsi richiesti")

## Metodo
def btnMetodoElencoOnClick():
    global metodo_PERCORSO_ELENCO
    metodo_PERCORSO_ELENCO = filedialog.askopenfilename(initialdir="./", title="Scegli file metodi pagamento",filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    LblElencoMetodo.config(text = metodo_PERCORSO_ELENCO)
def btnMetodoEseguiOnClick():
    try:
        global metodo_PERCORSO_ELENCO
        if(messagebox.askokcancel(message="Procedere?")):
            metodo.main(metodo_PERCORSO_ELENCO)
    except:
        messagebox.Message(message= "Selezionare percorsi richiesti")

## Timbro
def btnTimbroCartellaOnClick():
    global timbro_PERCORSO_CARTELLA
    timbro_PERCORSO_CARTELLA = filedialog.askdirectory(initialdir="./", title="Scegli cartella PDF") + "/"
    LblCartellaTimbro.config(text = timbro_PERCORSO_CARTELLA)
def btnTimbroMetodoOnClick():
    global timbro_PERCORSO_METODO
    timbro_PERCORSO_METODO = filedialog.askopenfilename(initialdir="./", title="Scegli file metodi pagamento",filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    LblMetodoTimbro.config(text = timbro_PERCORSO_METODO)
def btnTimbroNumeroOnClick():
    global timbro_PERCORSO_NUMERO
    timbro_PERCORSO_NUMERO = filedialog.askopenfilename(initialdir="./", title="Scegli file numeri fatture",filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    LblNumeroTimbro.config(text = timbro_PERCORSO_NUMERO)
def btnTimbroEseguiOnClick():
    try:
        global timbro_PERCORSO_CARTELLA, timbro_PERCORSO_METODO, timbro_PERCORSO_NUMERO
        if(messagebox.askokcancel(message="Procedere?")):
            timbro.main(timbro_PERCORSO_CARTELLA, timbro_PERCORSO_METODO, timbro_PERCORSO_NUMERO)
    except:
        messagebox.Message(message= "Selezionare percorsi richiesti")

# GUI

## Scheletro
root = Tk()
root.geometry("645x215")
root.resizable(FALSE,FALSE)
root.title("Clerk Buddy")
img = PhotoImage(file=resource_path("icon.png"))
root.iconphoto(TRUE, img)

body = Frame(root)
body.place(x=0, y=0, width=645, height=215)
logo = PhotoImage(file=resource_path("home.png"))
display = Label(body, image = logo)
display.place(x=180, y=30, width=400)

frameRinomina = Frame(body)
frameMetodo = Frame(body)
frameTimbro = Frame(body)

## Menu
frameMenu = Frame(body, bg="light grey")
btnMenu = Button(body, command = menu, text= "☰")
btnMenu.place(x=10, y=10)

menu_choice = StringVar()
radioRinomina = Radiobutton(frameMenu, bg="light grey", text = "Rinomina PDF", variable = menu_choice, value = "rinomina")
radioRinomina.place(x=10, y=10)
radioMetodo = Radiobutton(frameMenu, bg="light grey", text = "Trova metodo", variable = menu_choice, value = "metodo")
radioMetodo.place(x=10, y=30)
radioTimbro = Radiobutton(frameMenu, bg="light grey", text = "Timbra pagate", variable = menu_choice, value = "timbro")
radioTimbro.place(x=10, y=50)

## Rinomina

### Rinomina - Pulsanti
frameButtons = Frame(frameRinomina, bg="light grey")
frameButtons.place(x=40, y=10, width=170, height=95)

btnCartella = Button(frameButtons, width = 20, command = btnRinominaCartellaOnClick, text = "Seleziona cartella\ncon fatture")
btnCartella.place(x=10, y=10)
btnEsegui = Button(frameButtons, width = 20, command = btnRinominaEseguiOnClick, text = "Esegui")
btnEsegui.place(x=10, y=60)

### Rinomina - Labels
frameLabels = Frame(frameRinomina, bg="light grey")
frameLabels.place(x=225, y=10, width=400, height=60)

LblCartellaRinomina = Label(frameLabels, text="Percorso cartella")
LblCartellaRinomina.place(x=10, y=20)

## Metodo

### Metodo - Pulsanti
frameButtons = Frame(frameMetodo, bg="light grey")
frameButtons.place(x=40, y=10, width=170, height=95)

btnElenco = Button(frameButtons, width = 20, command = btnMetodoElencoOnClick, text = "Seleziona file\ncon elenco")
btnElenco.place(x=10, y=10)
btnEsegui = Button(frameButtons, width = 20, command = btnMetodoEseguiOnClick, text = "Esegui")
btnEsegui.place(x=10, y=60)

### Metodo - Labels
frameLabels = Frame(frameMetodo, bg="light grey")
frameLabels.place(x=225, y=10, width=400, height=60)

LblElencoMetodo = Label(frameLabels, text="Percorso Elenco")
LblElencoMetodo.place(x=10, y=20)

## Timbro

### Timbro - Pulsanti
frameButtons = Frame(frameTimbro, bg="light grey")
frameButtons.place(x=40, y=10, width=170, height=195)

btnCartella = Button(frameButtons, width = 20, command = btnTimbroCartellaOnClick, text = "Seleziona cartella\ncon fatture")
btnCartella.place(x=10, y=10)
btnMetodo = Button(frameButtons, width = 20, command = btnTimbroMetodoOnClick, text = "Seleziona file\ncon metodi pagamento")
btnMetodo.place(x=10, y=60)
btnNumero = Button(frameButtons, width = 20, command = btnTimbroNumeroOnClick, text = "Seleziona file\ncon numeri fatture")
btnNumero.place(x=10, y=110)
btnEsegui = Button(frameButtons, width = 20, command = btnTimbroEseguiOnClick, text = "Esegui")
btnEsegui.place(x=10, y=160)

### Timbro - Labels
frameLabels = Frame(frameTimbro, bg="light grey")
frameLabels.place(x=225, y=10, width=400, height=160)

LblCartellaTimbro = Label(frameLabels, text="Percorso cartella")
LblCartellaTimbro.place(x=10, y=20)
LblMetodoTimbro = Label(frameLabels, text="Percorso file")
LblMetodoTimbro.place(x=10, y=70)
LblNumeroTimbro = Label(frameLabels, text="Percorso file")
LblNumeroTimbro.place(x=10, y=120)

root.mainloop()