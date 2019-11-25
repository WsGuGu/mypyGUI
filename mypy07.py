#事件绑定
from tkinter import *


def a(a,b):
    print('a={0},b={1}'.format(a,b))


def b(event):
    print('输出')



root = Tk()
root.geometry('200x250+200+300')
g=Button(root,text='test',command=lambda: a(12,21))
g.pack(side='left')
Button(root,text='test',command=lambda: a(12,21)).pack(side='left')
Button(root,text='test',command=lambda: a(12,21)).pack(side='left')
g.bind_class('Button','<Button-2>',b)
root.mainloop()