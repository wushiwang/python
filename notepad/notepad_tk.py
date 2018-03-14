from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
import tkinter.messagebox as tkMessageBox

import os

def author():
    showinfo('作者信息','本软件有wushiwang完成')

def about():
    showinfo('版权信息','本软件由wushiwang所有')

def new():
    global filename
    root.title('未命名文件')
    filename=None
    textPad.delete(1.0,END)

def open():
    global filename
    filename=askopenfilename(defaultextension='.txt')
    if filename=='':
        filename=None
    else:
        root.title('FileName:'+ os.path.basename(filename))
        textPad.delete(1.0,END)
        with open(filename,'r') as f:
            textPad.insert(1.0,f.read())

def save_as():
    global filename
    filename = asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')
    with open(filename, 'w') as f:
        f.write(textPad.get(1.0, END))
    root.title('FileName: ' + os.path.basename(filename))

# 保存
def save():
    global filename
    try:
        with open(filename, 'w') as f:
            msg = textPad.get(1.0, END)
            print(msg)
            f.write(textPad.get(1.0, END))
        root.title('FileName: ' + os.path.basename(filename))
    except Exception as e:
        print(e.message)
        save_as()

def close():
    if tkMessageBox.askokcancel('Quit','文件没保存就退出？'):
        root.destroy()
    else:
        save_as()
        root.destroy()

# 剪切
def cut():
    textPad.event_generate('<<Cut>>')

# 复制
def copy():
    textPad.event_generate('<<Copy>>')

# 粘贴
def paste():
    textPad.event_generate('<<Paste>>')

# 撤销
def undo():
    textPad.event_generate('<<Undo>>')

# 重做
def redo():
    textPad.event_generate('<<Redo>>')

# 全选
def select_all():
    textPad.tag_add('sel',1.0, END)

# 搜索
def search(needle,cssnstv,textPad,t,e):
    textPad.tag_remove("match","1.0",END)
    count=0
    if needle:
        pos="1.0"
        while True:
            pos=textPad.search(needle,pos,nocase=cssnstv,stopindex=END)
            if not pos:break
            lastpos=pos+str(len(needle))
            textPad.tag_add("match",pos,lastpos)
            count+=1
            pos=lastpos
        textPad.tag_config('match')
        e.focus_set()
        t.title(str(count)+"个被匹配")
def find():
    t=Toplevel(root)
    t.title("查找")
    t.geometry("260x60+200+250")
    t.transient(root)
    Label(t,text="查找：").grid(row=0,column=0,sticky="e")
    v=StringVar()
    e=Entry(t,width=20,textvariable=v)
    e.grid(row=0,column=1,padx=2,pady=2,sticky="we")
    e.focus_set()
    c=IntVar()
    Checkbutton(t,text="不区分大小写",variable=c).grid(row=1,column=1,sticky='e')
    Button(t,text="查找所有",command=lambda:search(v.get(),c.get(),textPad,t,e)).grid(row=0,column=2,sticky="e"+"w",padx=2,pady=2)
    def close_search():
        textPad.tag_remove("match","1.0",END)
        t.destroy()
    t.protocol("WM_DELETE_WINDOW",close_search)





root= Tk()
root.title('记事本')
root.geometry('900x300+100+100')

menubar=Menu(root)
root.config(menu=menubar)

filemenu=Menu(menubar)
filemenu.add_command(label='新建',accelerator='Ctrl + N',command=new)
filemenu.add_command(label='打开',accelerator='Ctrl + O',command=open)
filemenu.add_command(label='保存',accelerator='Ctrl + S',command=save)
filemenu.add_command(label='另存为',accelerator='Ctrl + A',command=save_as)
filemenu.add_command(label='页面设置',accelerator='Ctrl + U')
filemenu.add_command(label='打印',accelerator='Ctrl + P')
filemenu.add_command(label='退出',accelerator='Ctrl + X',command=close)
menubar.add_cascade(label='文件',menu=filemenu)

editmenu=Menu(menubar)
editmenu.add_command(label='撤销',accelerator='Ctrl + Z',command=undo)
editmenu.add_command(label='重做',accelerator='Ctrl + Y',command=redo)
editmenu.add_command(label='剪切',accelerator='Ctrl + T',command=cut)
editmenu.add_command(label='复制',accelerator='Ctrl + C',command=copy)
editmenu.add_command(label='粘贴',accelerator='Ctrl + V',command=paste)
editmenu.add_command(label='查找',accelerator='Ctrl + F',command=find)
editmenu.add_command(label='替换',accelerator='Ctrl + H')
editmenu.add_command(label='全选',accelerator='Ctrl + A',command=select_all)
menubar.add_cascade(label='编辑',menu=editmenu)

abortmenu=Menu(menubar)
abortmenu.add_command(label='作者',command=author)
abortmenu.add_command(label='版权',command=about)
menubar.add_cascade(label='关于',menu=abortmenu)

status=Label(root,text='Ln20',bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

lnlabel=Label(root,width=2,bg='antique white')
lnlabel.pack(side=LEFT,fill=Y)
textPad=Text(root,undo=True)
textPad.pack(expand=YES,fill=BOTH)

scroll=Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT,fill=Y)
root.mainloop()


