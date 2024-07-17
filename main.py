from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import timbro
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

## Timbro
def btnCartellaOnClick():
    timbro_PERCORSO_CARTELLA = filedialog.askdirectory(initialdir="/", title="Scegli cartella PDF")
    LblCartella.config(text = timbro_PERCORSO_CARTELLA)
def btnMetodoOnClick():
    timbro_PERCORSO_METODO = filedialog.askopenfilename(initialdir="/", title="Scegli file metodi pagamento",filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    LblMetodo.config(text = timbro_PERCORSO_METODO)
def btnNumeroOnClick():
    timbro_PERCORSO_NUMERO = filedialog.askopenfilename(initialdir="/", title="Scegli file numeri fatture",filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    LblNumero.config(text = timbro_PERCORSO_NUMERO)
def btnEseguiOnClick():
    try:
        timbro.main(timbro_PERCORSO_CARTELLA, timbro_PERCORSO_NUMERO, timbro_PERCORSO_METODO)
    except:
        messagebox.Message(message= "Selezionare percorsi richiesti")




# GUI
root = Tk()
root.geometry("645x215")
root.title("Clerk Buddy")

frameRinomina = Frame(root)
frameMetodo = Frame(root)
frameTimbro = Frame(root)

## Menu
frameMenu = LabelFrame(root, text="", bg="light grey")
btnMenu = Button(root, command = menu, text= "☰")
btnMenu.place(x=10, y=10)
menu_choice = StringVar()
radioRinomina = Radiobutton(frameMenu, bg="light grey", text = "Rinomina PDF", variable = menu_choice, value = "rinomina")
radioRinomina.place(x=10, y=10)
radioMetodo = Radiobutton(frameMenu, bg="light grey", text = "Trova metodo", variable = menu_choice, value = "metodo")
radioMetodo.place(x=10, y=30)
radioTimbro = Radiobutton(frameMenu, bg="light grey", text = "Timbra pagate", variable = menu_choice, value = "timbro")
radioTimbro.place(x=10, y=50)

### Timbro - Pulsanti
frameButtons = LabelFrame(frameTimbro, text="", bg="light grey")
frameButtons.place(x=40, y=10, width=175, height=200)

btnCartella = Button(frameButtons, width = 20, command = btnCartellaOnClick, text = "Seleziona cartella\ncon fatture")
btnCartella.place(x=10, y=10)
btnMetodo = Button(frameButtons, width = 20, command = btnMetodoOnClick, text = "Seleziona file\ncon metodi pagamento")
btnMetodo.place(x=10, y=60)
btnNumero = Button(frameButtons, width = 20, command = btnNumeroOnClick, text = "Seleziona file\ncon numeri fatture")
btnNumero.place(x=10, y=110)
btnEsegui = Button(frameButtons, width = 20, command = btnEseguiOnClick, text = "Esegui")
btnEsegui.place(x=10, y=160)

### Timbro - Labels
frameLabels = LabelFrame(frameTimbro, text="", bg="light grey")
frameLabels.place(x=225, y=10, width=400, height=165)

LblCartella = Label(frameLabels, text="Percorso cartella")
LblCartella.place(x=10, y=20)
LblMetodo = Label(frameLabels, text="Percorso file")
LblMetodo.place(x=10, y=70)
LblNumero = Label(frameLabels, text="Percorso file")
LblNumero.place(x=10, y=120)

root.mainloop()