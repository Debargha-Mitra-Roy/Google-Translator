from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


def change(text="type", src="English", dest="Hindi"):

    textTemp = text
    srcTemp = src
    destTemp = dest
    trans = Translator()
    transTemp = trans.translate(text, src=srcTemp, dest=destTemp)
    return transTemp.text


def data():

    s = comboBox_source.get()
    d = comboBox_destination.get()
    msg = source_txt.get(1.0, END)
    textGet = change(text=msg, src=s, dest=d)
    destination_txt.delete(1.0, END)
    destination_txt.insert(END, textGet)


root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='Black')

lab_txt = Label(root, text="Translator", font=("Time New Roman", 40, "bold"))
lab_txt.place(x=100, y=40, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="Source Text", font=(
    "Time New Roman", 20, "bold"), fg="Red", bg="Black")
lab_txt.place(x=100, y=100, height=20, width=300)

source_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
source_txt.place(x=10, y=130, height=150, width=480)

list_text = list(LANGUAGES.values())

comboBox_source = ttk.Combobox(frame, value=list_text)
comboBox_source.place(x=10, y=300, height=40, width=150)
comboBox_source.set("english")

button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=170, y=300, height=40, width=150)

comboBox_destination = ttk.Combobox(frame, value=list_text)
comboBox_destination.place(x=330, y=300, height=40, width=150)
comboBox_destination.set("english")

lab_txt = Label(root, text="Destination Text", font=(
    "Time New Roman", 20, "bold"), fg="Red", bg="Black")
lab_txt.place(x=100, y=360, height=20, width=300)

destination_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
destination_txt.place(x=10, y=400, height=150, width=480)

root.mainloop()
