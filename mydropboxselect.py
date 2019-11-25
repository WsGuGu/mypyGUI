from tkinter import *
import os

def choose():
    """选择要存储的路径"""
    pass


def take(route):
    """拿取，已写完，需要得到路径"""
    try:
        os.system('adb devices')
        os.system('adb pull /data/system/dropbox {0}'.format(route))
    except BaseException:
        print('未找到dropbox')


def error():
    """弹出异常提示"""
    pass


def success():
    """弹出成功提示"""
    pass


if __name__=='__main__':
    root=Tk()
    root.title('日志小帮手')
    root.geometry('300x53+539+300')
    Button(root,text='选择...',command=choose,width=20).grid(row=1,column=0)
    Button(root,text='确定',command=take,width=20).grid(row=1,column=1)
    Label(root,text='未选择...',bg='yellow',width=40).grid(row=0,column=0,columnspan=2,sticky=NSEW)
    root.mainloop()