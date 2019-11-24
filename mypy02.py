from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()


    def createWidget(self):
        """创建组件"""
        self.btn01 = Button(self)
        self.btn01['text']='点击送花'
        self.btn01['command']=self.songhua
        self.btn01.pack()
        self.btnQuit = Button(self, text='退出', command=root.destroy)
        self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo('送花', '爪巴')


if  __name__ == '__main__':
   root=Tk()
   root.geometry('400x300+200+200')
   app=Application(root)
   root.mainloop()