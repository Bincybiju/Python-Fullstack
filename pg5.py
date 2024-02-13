from tkinter import *
w=Tk()
v1=BooleanVar()
v2=BooleanVar()
v3=BooleanVar()
u1=StringVar()
u2=StringVar()
u3=StringVar()
def disp():
    if v1.get():
        u1.set("Tasty Food")
    else:
        u1.set("Taste Not Upto Mark")
    if v2.get():
        u2.set("Nice packing")
    else:
        u2.set("Packing Not Upto Mark")

    if v3.get():
        u3.set("High speed delivery")
    else:
        u3.set("Delivery Speed Not Upto Mark")

    
l=Label(w,text="What did you like about our delivery : ",font="Times 12")
ch1=Checkbutton(w,text="Taste",variable=v1)
ch2=Checkbutton(w,text="packing",variable=v2)
ch3=Checkbutton(w,text="delivery speed",variable=v3)
l.place(x=100,y=30)
ch1.place(x=350,y=30)
ch2.place(x=350,y=60)
ch3.place(x=350,y=90)
Button(w,text="Click",command=disp).place(x=200,y=120)
l2=Label(w,textvariable=u1).place(x=200,y=150)
l3=Label(w,textvariable=u2).place(x=200,y=180)
l4=Label(w,textvariable=u3).place(x=200,y=210)
w.mainloop()




