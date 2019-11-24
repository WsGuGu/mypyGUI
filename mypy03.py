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
        self.label01 = Label(self, text='大哥大', width=10, height=2,
                             bg='black', fg='yellow', font=('黑体', 30))
        self.label01.pack()
        #显示图形
        # global photo
        # photo=PhotoImage(file='')
        # self.label03=Label(self, image=photo)
        # self.label03.pack()
        self.label04=Label(self,text='123\n321\n321',borderwidth=2,relief='solid',justify='right')
        self.label04.pack()
if __name__ == '__main__':
    root = Tk()
    root.geometry('400x300+200+200')
    app = Application(root)
    root.mainloop()
