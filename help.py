import tkinter as tk
import webbrowser
import time
import os
from datetime import date
from tkinter import *
from tkinter import Menu
from tkinter import messagebox as mb


#Рабочее окно
window = Tk()
window.title("Helper")
window.geometry('400x600')
window.resizable(width=False, height=False)
window.iconbitmap(r"C:\Users\Dmytro.Slobodian.PL03W169\Desktop\Helper\logo.ico")


#bg
C = Canvas(window, bg = "blue", height = 600, width = 400)
filename = PhotoImage(file = "C:\\Users\\Dmytro.Slobodian.PL03W169\\Desktop\\Helper\\BG2.png")
background_label = Label(window, image=filename)
background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
C.pack()


#Часы
def timing():
    current_time = time.strftime("%H : %M : %S")
    clock.config(text = current_time)
    clock.after(200, timing)

#Выход з приложения
def endProgram():
    raise SystemExit
    sys.exit()

#Кнопка информации
def show_info():
    msg = "Witam, ten program jest stworzony dla ułatwienia pracy na DEBUG | REPAIR. Był stworzony przez technika Dmytro Slobodian w wolnej chwilę od pracy.\nVersion: 0.3"
    mb.showinfo("Info", msg)

#Кнопка ошибки
def show_error():
    msg = "W danej chwilę pracujemy nad tym!"
    mb.showerror("Error", msg)

#Кнопка апгруйду
def show_info_up():
    msg = "Upd. Version 0.2: \nDodane Cookbook, Boomlista, menu Updating, możliwość robić refresh. Zrobiona możliwość dodawania aplikacji powyżej wszystkich okien oraz usunięcie tego. Dodane logo i zegar.\nUpd. Version 0.3:\nDodano date"
    mb.showinfo("Updating", msg)

#Обновить
def refresh():
    window.destroy()
    os.popen("help.py")

#Блокирование экрана
def block():
    window.attributes("-topmost", True)

#Разблокировка экрана
def unlock():
    window.attributes("-topmost", False)

#Гиперссылка
def callback(url):
    webbrowser.open_new(url)

def refresh_bi(event):
    window.destroy()
    os.popen("help.py")

#Флажки
r_var = BooleanVar()
r_var.set(0)


#Меню сверху
menu = Menu(window)
new_info = Menu(menu, tearoff = 0)
new_info.add_command(label = 'Info', command = show_info)
new_info.add_separator()
new_info.add_command(label = 'Seve', command = show_error)
new_info.add_command(label = 'Seve as...', command = show_error)
new_info.add_separator()
new_info.add_command(label = 'Refresh', command = refresh)
window.bind('<F5>', refresh_bi)
new_info.add_separator()
new_info.add_command(label = 'Settings', command = show_error)
new_info.add_separator()
new_info.add_command(label = "Exit", command = endProgram)
menu.add_cascade(label = 'File', menu = new_info)

new_comand = Menu(menu, tearoff = 0)
new_comand.add_command(label ='Alt + F4                     Exit')
new_comand.add_command(label ='Ctrl + S                     Save')
new_comand.add_command(label ='Ctrl + Shift + S        Save as')
new_comand.add_command(label ='Shift + F5                 Refresh')
menu.add_cascade(label = 'Commands', menu = new_comand)

new_window = Menu(menu, tearoff=0)
block_men = Menu(menu, tearoff=0)
block_men.add_radiobutton(label = "Lock", variable = r_var, value = 1, command = block)
block_men.add_radiobutton(label = 'Unlock', variable = r_var, value = 0, command = unlock)
new_window.add_cascade(label = 'Block window', menu = block_men)
new_window.add_separator()
lang_menu = tk.Menu(new_window, tearoff = 0)
lang_menu.add_command(label = 'Minimize all', command = show_error)
lang_menu.add_command(label = 'Closed all', command = show_error)
lang_menu.add_command(label = 'Full size all', command = show_error)
new_window.add_cascade(label = 'Size', menu = lang_menu)
new_window.add_separator()
new_window.add_command(label='Settings color', command = show_error)
menu.add_cascade(label = 'Window', menu = new_window)
window.config(menu = menu)

new_upd = Menu(menu, tearoff = 0)
menu.add_cascade(label = 'Updating', command = show_info_up)


#Заголовок
selected = IntVar()
lbl = Label(window, text="Co otworzyć:", bg = '#0c0c0c', fg = 'white', font=("Sylfaen", 26))
lbl.pack()
lbl.place(x=0, y=0)

#Times
clock=Label(window,font=("Sylfaen",18,"bold"),bg="#0c0c0c", fg = 'White')
clock.place(x = 250, y = 13)
timing()

#Data 
current_date = date.today().strftime("%d.%m.%Y")
lbl = Label(window, text= current_date, bg = "#0c0c0c", fg = 'White', font = ("Sylfaen", 10, "bold"))
lbl.pack()
lbl.place(x = 297, y = 40)

#Кликабельный текст
lbl = Label(window, text = "Outlook", bg = '#0c0c0c', fg = 'white', font = ("Sylfaen", 12))
lbl.pack()
lbl.bind("<Button-1>", lambda e: callback("https://outlook.office.com/mail/"))
lbl.place(x=0, y=50)

lbl = Label(window, text = "Kuna", bg = '#0c0c0c', fg = 'white', font = ("Sylfaen", 12))
lbl.pack()
lbl.bind("<Button-1>", lambda e: callback("http://kuna/index/"))
lbl.place(x=0, y=130)

lbl = Label(window, text = "Boom lista", bg = '#0c0c0c', fg = 'white', font = ("Sylfaen", 12))
lbl.pack()
lbl.bind("<Button-1>", lambda e: callback(r"file://\\tppl03s005\Resources\Operations\SKY\Repair\BOOM LISTA"))
lbl.place(x=0, y=110)

lbl = Label(window, text = "Cookbook", bg = '#0c0c0c', fg = 'white', font = ("Sylfaen", 12))
lbl.pack()
lbl.bind("<Button-1>", lambda e: callback(r"file://\\tppl03s005\Resources\Operations\SKY\Cookbook"))
lbl.place(x=0, y=90)

lbl = Label(window, text="Spot Check", bg = '#0c0c0c', fg = 'white', font=("Sylfaen", 12))
lbl.pack()
lbl.bind("<Button-1>", lambda e: callback(r"file://\\tppl03s005\Resources\Operations\SKY\Docs\Spot_Check"))
lbl.place(x=0, y=70)

lbl = Label(window, text="Portal", bg = '#0c0c0c', fg = 'white', font=("Sylfaen", 12))
lbl.pack()
lbl.bind("<Button-1>", lambda e: callback("http://portal2/"))
lbl.place(x=0, y=150)

lbl = Label(window, text="Schemat 150", bg = '#0c0c0c', fg = 'white', font=("Sylfaen", 12))
lbl.pack()
lbl.bind("<Button-1>", lambda e: callback(r"file://\\tppl03s005\Resources\Operations\SKY\Documentation\Dokumentacja_Techniczna\Q\info MrBox EM150\Schematics"))
lbl.place(x=0, y=170)

lbl = Label(window, text="Schemat 160", bg = '#0c0c0c', fg = 'white', font=("Sylfaen", 12))
lbl.pack()
lbl.bind("<Button-1>", lambda e: callback(r"file://\\tppl03s005\Resources\Operations\SKY\Documentation\Dokumentacja_Techniczna\Amidala\ESd-160s"))
lbl.place(x=0, y=190)

lbl = Label(window, text="Schemat 240", bg = '#0c0c0c', fg = 'white', font=("Sylfaen", 12))
lbl.pack()
lbl.bind("<Button-1>", lambda e: callback(r"file://\\tppl03s005\Resources\Operations\SKY\Documentation\Dokumentacja_Techniczna\Q\info ES240_ESi240\Schematics"))
lbl.place(x=0, y=210)

lbl = Label(window, text="Schemat 340", bg = '#0c0c0c', fg = 'white', font=("Sylfaen", 12))
lbl.pack()
lbl.bind("<Button-1>", lambda e: callback(r"file://\\tppl03s005\Resources\Operations\SKY\Documentation\Dokumentacja_Techniczna\Q\info Titan ES340"))
lbl.place(x=0, y=230)

#Подпись
lbl = Label(window, text="by Dmytro Slobodian", bg = '#131112', fg = 'white', font=("Sylfaen", 8))
lbl.pack()
lbl.bind("<Button-1>", lambda e: callback("mailto:dmytro.slobodian@reconext.com"))
lbl.place(x=290, y=560)

lbl = Label(window, text="form Debug | Repair", bg = '#262425', fg = 'white', font=("Sylfaen", 8))
lbl.pack()
lbl.bind("<Button-1>", lambda e: callback("https://www.reconext.com/"))
lbl.place(x=0, y=560)

window.mainloop()