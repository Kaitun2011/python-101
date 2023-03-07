from tkinter *
from tkinter ttk
from tkinter messagebox

GUI = Tk()
GUI.title('บันทึกราคารายรับค่าอินเตอร์เน็ต')
GUI.geonetry('500x500')

L1 = label(GUI,text='โปรแกรมบันทึกราคาผลไม้',font=('angsana New',32),fg='blue')
L1.place (x=25,y=50)



L2 = label(GUI,text='วันที่',font=('angsana New',20)fg='black')
L2.place (x=60,y=130)
E2 = ttk.Entry()
E2.place(s=160,y=10)

L3 = label(GUI,text='รายการผลไม้',font=('angsana New',20)fg='black')
L3.place (x=60,y=180)
E3 = ttk.entry()
E3.place(x=160,y=180)

L4 = label(GUI,text='รวมราคาผลไม้ได้ทั้งหมด',font=('angsana New',20)fg='black')
L4.place (x=60,y=230)
L6 = label(GUI,text='บาท',font=('angsana New',20)fg='black')
L6.place(x=-60,y=230)
E4 = ttk.Entry()
E4.place(x=160,y=230)

L5 = label(GUI,text='ชนิดผลไม้',font=('angsana New',20)fg='black')
L5.place(x=60,y=280)
E5 = ttk.Entry()
E5.place(x=160,y=280)


def Button() :
    text = 'บันทึกสำเร็จ'
    messagebox.showinfo('บันทึก',text)

B1 = ttk.Button(text='บันทึก',command=Button)
B1.place(x=220,y=350)
