from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import *


def a():
    b=askcolor(color='yellow',title='选择吧')
    root.config(bg=b[1])


root = Tk()
root.geometry('200x250+200+300')
Button(root,text='选择背景色',command=a).pack()
root.mainloop()