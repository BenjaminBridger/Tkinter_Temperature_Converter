import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext as st
from tkinter import filedialog
from tkinter import Menu


def export():
    print('export')


def settings():
    settings_window = Tk()
    settings_window.title("Temp Converter")
    settings_window.geometry('150x225')
    chk = Checkbutton(settings_window, text='AutoSave')
    chk.grid(column=2, row=0)
    print('window config')


def help_me():
    print('help')


def save():
    print('save to list')


# window
window = Tk()
window.title("Temp Converter")
window.geometry('300x450')


# top bar
menu = Menu(window)
new_item = Menu(menu, tearoff=0)
window.config(menu=menu)

menu.add_cascade(label='File', menu=new_item)
new_item.add_command(label='save to list', command=save)
new_item.add_command(label='export', command=export)
menu.add_command(label='Settings', command=settings)
menu.add_command(label='Help', command=help_me)




# ribbon
btn1 = Button(text='Export', command=export)
btn1.grid(column=0, row=0)
btn2 = Button(text=' Save ', command=save)
btn2.grid(column=1, row=0)
btn3 = Button(text=' Input', command=save)
btn3.grid(column=2, row=0)

# inputs
entry_c = tk.StringVar()
input_c = Entry(window, width=11)
entry_c.set('')
input_c.grid(column=0, row=2)

entry_f = tk.StringVar()
input_f = Entry(window, width=11)
entry_c.set('')
input_f.grid(column=1, row=2)

entry_k = tk.StringVar()
input_k = Entry(window, textvariable=entry_k, width=11)
entry_k.set('')
input_k.grid(column=2, row=2)


window.mainloop()