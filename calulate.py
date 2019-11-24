from tkinter import *



class Application():
    def __init__(self, master=None):
        frame = Frame(master)
        frame.pack()
        self.createWidget(frame)

    def createWidget(self, a):
        """创建组件"""
        btnText = (('MC', 'M+', 'M-', 'MR'),
                   ('C', '±', '/', 'X'),
                   (7, 8, 9, '-'),
                   (4, 5, 6, '+'),
                   (1, 2, 3, '='),
                   (0, '.'))
        Entry(a).grid(row=0, column=0, columnspan=4, pady=10)
        for rindex, r in enumerate(btnText):
            for cindex, c in enumerate(r):
                if c == '=':
                    Button(a, text=c, width=2).grid(row=rindex + 1, column=cindex, rowspan=2, sticky=NSEW)
                elif c == 0:
                    Button(a, text=c, width=2).grid(row=rindex + 1, column=cindex, columnspan=2, sticky=NSEW)
                elif c == '.':
                    Button(a, text=c, width=2).grid(row=rindex + 1, column=cindex+1, sticky=NSEW)
                else:
                    Button(a, text=c, width=2).grid(row=rindex + 1, column=cindex, sticky=NSEW)


if __name__ == '__main__':
    root = Tk()
    root.geometry('200x250+200+300')
    root.title('calculate')
    app = Application(root)
    root.mainloop()