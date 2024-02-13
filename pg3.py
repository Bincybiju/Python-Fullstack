from tkinter import *
w=Tk()
c=Canvas(w,height=500,width=500,bg="yellow")
coord=100,50,500,300
arc=c.create_arc(coord,start=0,extent=120,fill="red")
c.pack()
w.mainloop()
