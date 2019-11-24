from tkinter import *
from tkinter import messagebox


def abc(e):
    messagebox.showinfo('想得美', '给爷爪巴')


root = Tk()
root.title('我的第一个gui')
root.geometry('500x200+400+200')
btn01 = Button(root)
btn01['text'] = '点击送钱'
btn01.bind('<Button-1>', abc)
btn01.pack()
root.mainloop()  # 进入事件循环
