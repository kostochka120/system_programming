from tkinter import *
from tkinter import messagebox
global a, b
root = Tk()

def summ(event):
    func()
    s = a+b
    s = str(s)
    lab['text'] = ' '.join(s)

def minus(event):
    func()
    s = a-b
    s = str(s)
    lab['text'] = ' '.join(s)

def mult(event):
    func()
    s = a*b
    s = str(s)
    lab['text'] = ' '.join(s)

def div(event):
    func()
    s = a/b
    s = str(s)
    lab['text'] = ' '.join(s)

def func():
    try:
        global a, b
        a = ent.get()
        a = int(a)
        b = ent1.get()
        b = int(b)
    except ValueError:
        messagebox.showerror("ОШИБКА", "введите число")

ent = Entry(width=25)
ent1 = Entry(width=25)
but = Button(text="+", width=10)
but2 = Button(text="-", width=10)
but3 = Button(text="*", width=10)
but4 = Button(text="/", width=10)
lab = Label(width=20, bg='gray', fg='white')


but.bind('<Button-1>', summ)
but2.bind('<Button-1>', minus)
but3.bind('<Button-1>', mult)
but4.bind('<Button-1>', div)

ent.pack()
ent1.pack()
but.pack()
but2.pack()
but3.pack()
but4.pack()
lab.pack()
root.mainloop()