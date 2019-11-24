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
        self.label01 = Label(self, text='用户名')
        self.label01.grid(row=0, column=0)
        user = StringVar()
        self.a1 = Entry(self, textvariable=user)
        self.a1.grid(row=0,column=1)
        self.label02 = Label(self, text='密码')
        self.label02.grid(row=1,column=0)
        pwd = StringVar()
        self.a2 = Entry(self, textvariable=pwd, show='*')
        self.a2.grid(row=1,column=1)
        self.btnQuit = Button(self, text='退出', command=root.destroy)
        self.btnQuit.grid(row=2,column=2)
        Button(self, text='登录', command=self.login).grid(row=2,column=1,sticky=NSEW)

    def login(self):
        messagebox.showinfo('登录窗口', '成功')
        print(self.a1.get())
        print(self.a2.get())


if __name__ == '__main__':
    root = Tk()
    root.geometry('300x100+200+200')
    app = Application(root)
    root.mainloop()