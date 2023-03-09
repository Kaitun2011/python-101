from tkinter import *
from tkinter import ttk
from tkinter import messagebox


GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย')
GUI.geonetry('500')

L1 = label(GUI,text='โปรแกรมบันทกค่าใช้จ่ายประจำวัน',font=('angsana New',32),fg='black')
L1.place(x=25,y=50)




L2 = label(GUI,text='วันที่',font=('angsana New',20),fg='black')
L2.place(x=60,y=130)
E2 = ttk.Entry()
E2.place(x=160,y=10)

L3 = label(GUI,text='รายการ',font=('angsana New',20),fg='black')
L3.place(x=60,y=180)
E3 = ttk.Entry()
E3.place(x=160,y=180)

L4 = label(GUI,text='จำนวนเงินที่ใช้ไป',font=('angsana New',20),fg='black')
L4.place(x=60,y=230)
L6 = label(GUI,text='บาท',font=('angsana New',20),fg='black')
L6.place(x=360,y=230)
E4 = ttk.Entry()
E4.place(x=160,y=230)


L5 = label(GUI,text='ประเภท',font=('angsana New',20),fg='black')
L5.place(x=60,y=280)
combo1 = ttk.combobox(value=["ช้อบปิง","อาหาร","ค่าเดินทาง","ของใช้ในบ้าน","อื้น"])
combo1.place(x=160,y=280)


def button() :
    text = 'บันทึกสำเร็จ'
    messagebox.showinfo('บันทึก',text)

B1 = ttk.Button(text='บันทึก', command=button)
B1.place(x=220,y=350)

GUI.mainloop()
