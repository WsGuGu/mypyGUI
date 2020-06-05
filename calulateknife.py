from math import ceil
from tkinter.filedialog import *
from tkinter.messagebox import *


def selectOne():
    "符合情况的执行该方法"
    select = conv.get()
    if select == "合刀boss中途死亡":
        damageKilled()
    elif select == "合刀boss未中途死亡":
        mergeDamage()
    else:
        showerror("错误", "请选择模式")


def mergeDamage():
    "未中途死亡，计算合刀的剩余时间，将之转为x:xx显示"
    try:
        boss = int(bossEntry.get())
        damage = int(damageEntry.get())
        returntime = ceil((1 - (boss / damage)) * 90 + 10)
        minute = int(returntime / 60)
        seconds = returntime % 60
        if returntime > 90:
            showinfo("结果", "剩余时间{}:{}，实际返还时间1:30，请注意模拟补偿刀的伤害".format(minute, seconds))
        elif returntime < 10:
            showinfo("结果", "剩余时间{}:{}，数值错误".format(minute, seconds))
        else:
            showinfo("结果", "剩余时间{}:{}，请注意模拟补偿刀的伤害".format(minute, seconds))
    except:
        showerror("错误", "数据错误，请输入数值")


def damageKilled():
    "中途死亡，计算合刀的剩余时间，将之转为x:xx显示"
    try:
        boss = int(bossEntry.get())
        damage = int(damageEntry.get())
        time = int(timeEntry.get())
        returntime = ceil((time / 90 - (boss / damage)) * 90 + 10)
        minute = int(returntime / 60)
        seconds = returntime % 60
        if returntime > 90:
            showinfo("结果", "剩余时间{}:{}，实际返还时间1:30，请注意模拟补偿刀的伤害".format(minute, seconds))
        elif returntime <= 10:
            showinfo("结果", "剩余时间{}:{}，数值错误".format(minute, seconds))
        else:
            showinfo("结果", "剩余时间{}:{}，请注意模拟补偿刀的伤害".format(minute, seconds))
    except:
        showerror("错误", "数据错误，请输入数值")


if __name__ == '__main__':
    root = Tk()
    root.title('咕咕的合刀时间计算')
    root.geometry('330x165+539+300')
    boss = Label(root, text="boss剩余HP", width=25)
    bossEntry = Entry(root)
    damage = Label(root, text="造成伤害", width=25)
    damageEntry = Entry(root)
    time = Label(root, text="消耗时间(打死boss)", width=25)
    exp = StringVar()
    timeEntry = Entry(root, textvariable=exp)
    exp.set("boss中途死亡，输入数字")
    cal = Button(root, text='计算合刀', command=lambda: selectOne(), width=15)
    conv = StringVar(root)
    conv.set('选择某种情况')
    op = OptionMenu(root, conv, '合刀boss未中途死亡', "合刀boss中途死亡")
    boss.grid(row=1, column=1)
    bossEntry.grid(row=2, column=1)
    damage.grid(row=3, column=1)
    damageEntry.grid(row=4, column=1)
    time.grid(row=5, column=1)
    timeEntry.grid(row=6, column=1)
    cal.grid(row=7, column=2)
    op.grid(row=7, column=1)
    root.resizable(0, 0)
    root.mainloop()