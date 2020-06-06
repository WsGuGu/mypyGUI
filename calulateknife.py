from math import ceil
from tkinter.filedialog import *
from tkinter.messagebox import *


def selectOne():
    """选择一种出现的情景，并且执行相应的函数进行计算"""
    select = conv.get()
    if select == "合刀boss中途死亡":
        testKilled()
    elif select == "合刀boss未中途死亡":
        testDamage()
    else:
        showerror("错误", "请选择模式")


def mergeDamage(boss, damage):
    """未中途死亡，计算合刀的剩余时间，将之转为x:xx显示，返回一个列表[minute,seconds,returntime]"""
    if boss > 0 and damage > 0:
        returntime = ceil((1 - (boss / damage)) * 90 + 10)
        minute = int(returntime / 60)
        seconds = returntime % 60
        return [minute, seconds, returntime]


def damageKilled(boss, damage, time):
    """中途死亡，计算合刀的剩余时间，将之转为x:xx显示，返回一个列表[minute,seconds,returntime]"""
    if boss > 0 and damage > 0 and time > 0:
        returntime = ceil((time / 90 - (boss / damage)) * 90 + 10)
        minute = int(returntime / 60)
        seconds = returntime % 60
        return [minute, seconds, returntime]


def testDamage():
    """在中途未死亡的情况下计算补偿时间，并根据条件判断，返回相应的提示"""
    try:
        boss = int(bossEntry.get())
        firstdamage = int(damage1Entry.get())
        seconddamage = int(damage2Entry.get())
        firstout = boss - seconddamage
        secondout = boss - firstdamage
        firstlist = mergeDamage(firstout, firstdamage)
        secondlist = mergeDamage(secondout, seconddamage)
        if firstlist[2] > 90 and firstdamage > 0 and seconddamage > 0:
            showinfo("结果", "造成{}伤害，剩余时间{}:{}，实际返还时间1:30，请注意模拟补偿刀的伤害".format(firstdamage, firstlist[0], firstlist[1]))
        elif 10 <= firstlist[2] <= 90 and firstdamage > 0 and seconddamage > 0:
            showinfo("结果", "造成{}伤害，剩余时间{}:{}，请注意模拟补偿刀的伤害".format(firstdamage, firstlist[0], firstlist[1]))
        else:
            showerror("结果", "造成{}伤害，剩余时间{}:{}，数值错误".format(firstdamage, firstlist[0], firstlist[1]))
        if secondlist[2] > 90 and firstdamage > 0 and seconddamage > 0:
            showinfo("结果", "造成{}伤害，剩余时间{}:{}，实际返还时间1:30，请注意模拟补偿刀的伤害".format(seconddamage, secondlist[0], secondlist[1]))
        elif 10 <= secondlist[2] <= 90 and firstdamage > 0 and seconddamage > 0:
            showinfo("结果", "造成{}伤害，剩余时间{}:{}，请注意模拟补偿刀的伤害".format(seconddamage, secondlist[0], secondlist[1]))
        else:
            showerror("结果", "造成{}伤害，剩余时间{}:{}，数值错误".format(seconddamage, secondlist[0], secondlist[1]))
    except:
        showerror("错误", "伤害数值错误")


def testKilled():
    """在中途死亡的情况下计算补偿时间，并根据条件判断，返回相应的提示"""
    try:
        boss = int(bossEntry.get())
        firstdamage = int(damage1Entry.get())
        seconddamage = int(damage2Entry.get())
        firsttime = int(time1Entry.get())
        secondtime = int(time2Entry.get())
        firstout = boss - seconddamage
        secondout = boss - firstdamage
        firstlist = damageKilled(firstout, firstdamage, firsttime)
        secondlist = damageKilled(secondout, seconddamage, secondtime)
        if firstlist[
            2] > 90 and firstdamage > 0 and seconddamage > 0 and firsttime > 0 and secondtime > 0 and firstout > 0:
            showinfo("结果", "造成{}伤害，剩余时间{}:{}，实际返还时间1:30，请注意模拟补偿刀的伤害".format(firstdamage, firstlist[0], firstlist[1]))
        elif 10 < firstlist[
            2] <= 90 and firstdamage > 0 and seconddamage > 0 and firsttime > 0 and secondtime > 0 and firstout > 0:
            showinfo("结果", "造成{}伤害，剩余时间{}:{}，请注意模拟补偿刀的伤害".format(firstdamage, firstlist[0], firstlist[1]))
        else:
            showerror("结果", "造成{}伤害，剩余时间{}:{}，数值错误".format(firstdamage, firstlist[0], firstlist[1]))
        if secondlist[
            2] > 90 and seconddamage > 0 and seconddamage > 0 and firsttime > 0 and secondtime > 0 and secondout > 0:
            showinfo("结果", "造成{}伤害，剩余时间{}:{}，实际返还时间1:30，请注意模拟补偿刀的伤害".format(seconddamage, secondlist[0], secondlist[1]))
        elif 10 < secondlist[
            2] <= 90 and firstdamage > 0 and seconddamage > 0 and firsttime > 0 and secondtime > 0 and secondout > 0:
            showinfo("结果", "造成{}伤害，剩余时间{}:{}，请注意模拟补偿刀的伤害".format(seconddamage, secondlist[0], secondlist[1]))
        else:
            showerror("结果", "造成{}伤害，剩余时间{}:{}，数值错误".format(seconddamage, secondlist[0], secondlist[1]))
    except:
        showerror("错误", "伤害数值错误")


if __name__ == '__main__':
    root = Tk()
    root.title('咕咕的合刀时间计算')
    root.geometry('350x165+539+300')
    boss = Label(root, text="boss剩余HP", width=25)
    bossEntry = Entry(root)
    damage1 = Label(root, text="第一刀造成伤害", width=25)
    damage1Entry = Entry(root)
    time1 = Label(root, text="第一刀消耗时间(打死boss)", width=25)
    exp1 = StringVar()
    time1Entry = Entry(root, textvariable=exp1)
    exp1.set("boss中途死亡，输入数字")
    damage2 = Label(root, text="第二刀造成伤害", width=25)
    damage2Entry = Entry(root)
    time2 = Label(root, text="第二刀消耗时间(打死boss)", width=25)
    exp2 = StringVar()
    time2Entry = Entry(root, textvariable=exp2)
    exp2.set("boss中途死亡，输入数字")
    cal = Button(root, text='计算合刀', command=lambda: selectOne(), width=15)
    conv = StringVar(root)
    conv.set('选择某种情况')
    op = OptionMenu(root, conv, '合刀boss未中途死亡', "合刀boss中途死亡")
    boss.grid(row=1, column=1, columnspan=2)
    bossEntry.grid(row=2, column=1, columnspan=2)
    damage1.grid(row=3, column=1)
    damage1Entry.grid(row=4, column=1)
    time1.grid(row=5, column=1)
    time1Entry.grid(row=6, column=1)
    damage2.grid(row=3, column=2)
    damage2Entry.grid(row=4, column=2)
    time2.grid(row=5, column=2)
    time2Entry.grid(row=6, column=2)
    cal.grid(row=7, column=2)
    op.grid(row=7, column=1)
    root.resizable(0, 0)
    root.mainloop()
