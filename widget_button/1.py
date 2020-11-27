from tkinter import *

root = Tk()
label = Label(width=15)
code = Entry(text='Код', width=15)
code.insert(0, 'Код')
label['text'] = 'Цвет'

def red():
    code.delete(0, END)
    code.insert(0, "#ff0000")
    label['text'] = 'Красный'
def orange():
    code.delete(0, END)
    code.insert(0, "#FFA500")
    label['text'] = 'Оранжевый'
def yellow():
    code.delete(0, END)
    code.insert(0, "#FFFF00")
    label['text'] = 'Жёлтый'
def green():
    code.delete(0, END)
    code.insert(0, "#00FF00")
    label['text'] = 'Зелёный'
def sky():
    code.delete(0, END)
    code.insert(0, "#00FFFF")
    label['text'] = 'Голубой'
def blue():
    code.delete(0, END)
    code.insert(0, "#0000FF")
    label['text'] = 'Синий'
def purple():
    code.delete(0, END)
    code.insert(0, "#800080")
    label['text'] = 'Фиолетовый'


but = Button(bg='#ff0000', command=red, width=15,)
but2 = Button(bg='#FFA500', command=orange, width=15)
but3 = Button(bg='#FFFF00', command=yellow, width=15)
but4 = Button(bg='#00FF00', command=green, width=15)
but5 = Button(bg='#00FFFF', command=sky, width=15)
but6 = Button(bg='#0000FF', command=blue, width=15)
but7 = Button(bg='#800080', command=purple, width=15)
label.pack()
code.pack()
but.pack()
but2.pack()
but3.pack()
but4.pack()
but5.pack()
but6.pack()
but7.pack()
root.mainloop()