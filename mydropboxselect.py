import subprocess
from tkinter.filedialog import *
from tkinter.messagebox import *

rt = None
div = None


def choose():
    """选择要存储的路径"""
    f = askdirectory()
    display['text'] = f
    global rt
    rt = f


def take(route):
    """拿取"""
    try:
        div = device1.get()
        subprc = subprocess.Popen(r'adb -s {0} root'.format(div),
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
        output = subprc.communicate()
        message2 = output[0].decode('gbk')
        if 'adbd cannot run as root ' in message2:
            showerror('错误', '手机缺少root权限')
        else:
            subprc = subprocess.Popen(r'adb -s {0} pull /data/system/dropbox {1}\dropbox'.format(div, route),
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
            output = subprc.communicate()
            message = output[1].decode('gbk')
            if 'device not found' in message or 'does not exist' in message:
                showerror('重试', '未找到dropbox')
            else:
                if rt is None or rt == '':
                    showerror('错误', '路径不能为空')
                else:
                    showinfo('成功', 'DropBox导入成功')
    except:
        showerror('异常', '未选择设备')


def gugu():
    showinfo('信息', '     WildGuGu   \nQQ:1273036191')


def gets():
    """取得设备"""
    lots = []
    n = 0
    cmd = 'adb devices'
    subprc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = subprc.communicate()
    a = output[0].decode('gbk')
    b = a.split()
    while n < (len(b) - 4) / 2:
        lots.append(b[4 + 2 * n])
        n += 1
    global device1
    device1 = StringVar(root)
    device1.set('选择某个设备')
    st1 = OptionMenu(root, device1, '选择某个设备', *lots)
    st1.grid(row=2, column=0, columnspan=2, sticky=NSEW)


if __name__ == '__main__':
    root = Tk()
    root.title('咕咕的日志小帮手--DropBox')
    root.geometry('300x115+539+300')
    select = Button(root, text='选择...', command=choose, width=20)
    select.grid(row=1, column=0)
    draw = Button(root, text='提取', command=lambda: take(rt), width=20)
    draw.grid(row=1, column=1)
    display = Label(root, text='未选择...', bg='white', width=40)
    display.grid(row=0, column=0, columnspan=2, sticky=NSEW)
    device = StringVar(root)
    device.set('选择某个设备')
    op = OptionMenu(root, device, '选择某个设备')
    op.grid(row=2, column=0, columnspan=2, sticky=NSEW)
    refrash = Button(root, text='更新下拉框', command=gets, width=20)
    refrash.grid(row=3, column=1)
    about = Button(root, text='关于', command=gugu, width=20)
    about.grid(row=3, column=0)
    root.resizable(0, 0)
    showwarning('注意', '请检查是否与手机连接,并且有root权限')
    root.mainloop()