from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
# from tkinter import PhotoImage
w=Tk()
w.geometry('600x600')
v=StringVar()
vv=StringVar()

v1=StringVar()
v2=StringVar()
v3=BooleanVar()
v4=BooleanVar()
v5=BooleanVar()
v6=StringVar()
v7=StringVar()

u=StringVar()
u1=StringVar()
u2=StringVar()
u4=StringVar()
u5=StringVar()
u6=StringVar()
u7=StringVar()
u8=StringVar()
u9=StringVar()
u10=StringVar()


m=StringVar()
n=StringVar()

def disp():
    u.set(v.get())
    u1.set(v1.get())
    u2.set(v2.get())
    u4.set(m.get())
    u5.set(vv.get())
    u6.set(n.get())

    if v3.get():
        u7.set("Front-end projects")
    else:
        u7.set("Front-end projects Not Upto Mark")
    if v4.get():
        u8.set("Back-end projects")
    else:
        u8.set("Back-end projects Not Upto Mark")

    if v5.get():
        u9.set("Data visualization")
    else:
        u9.set("Data visualization Not Upto Mark")
    u10.set(e3.get(1.0,END))
   




# bg_image = Image.open("C:\\Users\\bincy\\OneDrive\\Pictures\\p.jpeg")  # Replace with your image file
# screen_width = w.winfo_screenwidth()
# screen_height = w.winfo_screenheight()
# bg_image = bg_image.resize((screen_width, screen_height), Image.LANCZOS)
# bg_photo = ImageTk.PhotoImage(bg_image)
# bg_label = Label(w, image=bg_photo)
# bg_label.place(relwidth=1, relheight=1)

l1=Label(w,text="SURVEY FORM",font="Times 16",compound="center").pack()

f=Frame(w).place(x=320,y=60,height=700,width=900)

# li=Label(f,text="\n\nLet us know how we can improve ",font="Times 12").pack()

l1=Label(f,text="Name :",font="Times 12").place(x=650,y=100)
e=Entry(f,textvariable=v)
v.set("Name")
e.bind("<Button-1>",lambda n : e.delete(0,END))
e.place(x=700,y=100)

l2=Label(f,text="Email :",font="Times 12").place(x=650,y=150)
e1=Entry(f,textvariable=v1)
v1.set("Email")
e1.bind("<Button-1>",lambda n : e1.delete(0,END))
e1.place(x=700,y=150)

l3=Label(f,text="Age :",font="Times 12").place(x=650,y=200)
e2=Entry(f,textvariable=v2)
v2.set("Age")
e2.bind("<Button-1>",lambda n : e2.delete(0,END))
e2.place(x=700,y=200)

Button(f,text="Choose File").place(x=700,y=250)
l4=Label(f,text="No file chosen ",font="Times 12").place(x=770,y=250)

l5=Label(f,text="Which option best describes your current role? ",font="Times 12").place(x=400,y=300)
c=ttk.Combobox(f,value=["Java intern","python intern","Embedded"],textvariable=m).place(x=700,y=300)

l6=Label(f,text="How likely is that you would recommend this \n program to a friend? ",justify="right",font="Times 12").place(x=420,y=350)
r=Radiobutton(f,text="Definitely",variable=vv,value="Definitely").place(x=700,y=350)
r1=Radiobutton(f,text="Maybe",variable=vv,value="Maybe").place(x=700,y=380)
r2=Radiobutton(f,text="Not sure",variable=vv,value="Not sure").place(x=700,y=410)

l7=Label(f,text="What do you like most here? ",font="Times 12").place(x=500,y=460)
ttk.Combobox(f,value=["Friendly atmosphere","Better teaching"],textvariable=n).place(x=700,y=460)

l8=Label(f,text="Things that should be improved in the future \n (Check all that apply): ",justify='right',font="Times 12").place(x=420,y=510)
ch1=Checkbutton(f,text="Front-end Projects",variable=v3).place(x=700,y=510)
ch2=Checkbutton(f,text="Back-end Projects",variable=v4).place(x=700,y=540)
ch3=Checkbutton(f,text="Data visualization",variable=v5).place(x=700,y=570)

l9=Label(f,text="Any comments or Suggestions? ",font="Times 12").place(x=500,y=620)

e3=Text(f)
Fact="Enter your comment here..."
e3.insert(END, Fact)
e3.bind("<Button-1>",lambda n : e3.delete("1.0","end"))
e3.place(x=700,y=620,height=50,width=250)

Button(f,text="Submit",bg="blue",command=disp).place(x=700,y=700)

li=Label(w,textvariable=u).place(x=1000,y=100)
li1=Label(w,textvariable=u1).place(x=1000,y=130)
li2=Label(w,textvariable=u2).place(x=1000,y=160)
li4=Label(w,textvariable=u4).place(x=1000,y=210)
li5=Label(w,textvariable=u5).place(x=1000,y=240)
li6=Label(w,textvariable=u6).place(x=1000,y=270)
li7=Label(w,textvariable=u7).place(x=1000,y=300)
li8=Label(w,textvariable=u8).place(x=1000,y=330)
li9=Label(w,textvariable=u9).place(x=1000,y=360)
li10=Label(w,textvariable=u10).place(x=1000,y=390)





w.mainloop()
