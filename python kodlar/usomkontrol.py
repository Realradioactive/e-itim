from tkinter import *
import datetime
def kontrol_et():
    print("test")
    dosya=open("usom.txt","r")
    içerik=dosya.read()
    dosya.close()
    ip=entry1.get()
    bugün=datetime.datetime.now()
    if str(ip) in içerik:
        dosya=open("log.txt","a")
        yazi=str(ip)+"zararli\nTarih:"+str(bugün)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("İp Zararlıdır")
    else:
        dosya=open("log.txt","a")
        yazi=str(ip)+ " zararli değil\nTarih:"+str(bugün)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("İp Temiz")

top=Tk()
top.title("Usom ip kontrol")
B=Button(top,text="kontrol et",command=kontrol_et)
B.place(x=50,y=50)
B.pack()
label1=Label(top,text="kontrol edilecek ip adresini gir:")
label1.place(x=50,y=90)
label1.pack()
entry1=Entry(top)
entry1.place(x=50,y=50)
entry1.pack()
v=StringVar()
entry2=Entry(top,textvariable=v)
entry2.place(x=50,y=110)
entry2.pack()
top.mainloop()