from tkinter import *
w=Tk()
v=StringVar()
l1=StringVar()
def disp():
    l1.set(v.get())
l=Label(w,text="choose your gender",font="Times 12")
r=Radiobutton(w,text="Male",variable=v,value="M")
r1=Radiobutton(w,text="Female",variable=v,value="F")
r2=Radiobutton(w,text="Others",variable=v,value="O")
l.place(x=100,y=30)
r.place(x=350,y=30)
r1.place(x=350,y=60)
r2.place(x=350,y=90)
Button(w,text="Click",command=disp).place(x=200,y=120)
l2=Label(w,textvariable=l1).place(x=200,y=150)
w.mainloop()

