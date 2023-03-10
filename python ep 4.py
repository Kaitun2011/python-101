from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
##############CSV###############
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser']


def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data
#############################

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อโปรแกรม
GUI.geometry('900x400') #นี่คือขนาดโปรแกรม

L1 = Label(GUI,text='โปรแกรมบันทึกข้อมูล',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)
####################
def Button2():
    text = ('ตอนนี้มีเงินในบัญชีอยู่ 5000 บาท')
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=180)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)
####################
def Button3():
    text = ('Math','english','science')
    messagebox.showinfo('วิชาเรียนสัปดาร์นี้',text)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=100,y=230)
B3 = ttk.Button(FB1,text='สัปดาห์เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20)

##########SECTION RIGHT##########
LF1 = ttk.LabelFrame(GUI,text='กรอกข้อมูลที่ต้องการเข้าไป')
LF1.place(x=400,y=50)

v_data = StringVar() # ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',25))
E1.pack(pady=10,padx=10)

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t,data] # [เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง csv
    v_data.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก

B4 = ttk.Button(LF1,text='บันทึก',command=SaveData)
B4.pack(ipadx=20,ipady=20)



GUI.mainloop()
