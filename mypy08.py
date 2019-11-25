from tkinter import *


def a(value):
    print('等于',value)
    b.config(font=('宋体',value))



root = Tk()
root.geometry('200x250+200+300')
Scale(root,from_=10,to=50,length=200,tickinterval=5,orient=HORIZONTAL,command=a).pack()
b=Label(root,text='11111',bg='white')
b.pack()

root.mainloop()