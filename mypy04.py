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
        self.label01.pack()
        user = StringVar()
        self.a1 = Entry(self, textvariable=user)
        self.a1.pack()
        self.label02 = Label(self, text='密码')
        self.label02.pack()
        pwd = StringVar()
        self.a2 = Entry(self, textvariable=pwd, show='*')
        self.a2.pack()
        self.btnQuit = Button(self, text='退出', command=root.destroy)
        self.btnQuit.pack()
        Button(self, text='登录', command=self.login).pack()

    def login(self):
        messagebox.showinfo('登录窗口', '成功')
        print(self.a1.get())
        print(self.a2.get())


if __name__ == '__main__':
    root = Tk()
    root.geometry('400x300+200+200')
    app = Application(root)
    root.mainloop()