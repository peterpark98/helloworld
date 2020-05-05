from tkinter import *
from tkinter.filedialog import*
import os
def selectPath():
    path_ = askdirectory()
    path.set(path_)

def selectFile():
    path_ = askopenfilename()
    path1.set(path_)
def readname():
    name = os.listdir(path.get())
    return name
def textname():
    a = []
    for line in open(path1.get(),'r',encoding = 'UTF-8'):
        rs = line.rstrip('\n')
        a.append(rs)
    return a
def result():
    total = 0
    name = readname()
    tname = textname()
    for i in name:
        for j in tname:
            if j in i:
                total += 1
                tname.remove(j)
                break
#    print(tname)
#    print(total)
    listb = Listbox(root)
    for k in tname:
        listb.insert(0,k)
    listb.place(y=250,x=120,width = 200 ,height = 200)

root = Tk()
path = StringVar()
path1 = StringVar()
lb1=Label(root,text = "目标路径:").place(y = 50, x = 50)
ent1=Entry(root, textvariable = path).place(y = 50, x = 120,width = 200)
bt1=Button(root, text = "路径选择", command = selectPath).place(y = 45, x =330)
bt2=Button(root, text = "查询",command = result).place(y = 150, x =180,width = 90 ,height = 50)

lb2=Label(root,text = "名单路径:").place(y = 90, x = 50)
ent1=Entry(root, textvariable = path1).place(y = 90, x = 120,width = 200)
bt3 = Button(root, text = "名单选择", command = selectFile).place(y = 90, x =330)

root.resizable(0,0)
root.attributes("-alpha",0.8)
root.title('作业名单查询器')
root.geometry('450x500+800+300')
root.mainloop()