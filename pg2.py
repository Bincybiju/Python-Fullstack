# from tkinter import *
# w=Tk()
# v=StringVar()
# def disp():
#     print(v.get())
# e=Entry(w,textvariable=v)
# e.pack()
# b=Button(w,text="submit",bg="black",fg="white",command=disp).pack()
# w.mainloop()

from tkinter import *
w=Tk()
v=StringVar()
l1=StringVar()
def disp():
    x=v.get()
    l1.set(x)
e=Entry(w,textvariable=v)
e.pack()
b=Button(w,text="submit",bg="red",fg="white",command=disp).pack()
l=Label(w,textvariable=l1)
l.pack()
w.mainloop()







