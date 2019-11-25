from tkinter import *


def a(a,b):
    print('a={0},b={1}'.format(a,b))


root = Tk()
root.geometry('200x250+200+300')
Button(root,text='test',command=lambda: a(12,21)).pack()
root.mainloop()