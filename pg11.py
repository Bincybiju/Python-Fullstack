import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    port='3306',
    password="root",
    database="phonebook"
)
print("connection established")
mycursor=mydb.cursor()
# mycursor.execute("create table phone(name varchar(50),phonenumber int)")
# print("Table created")

from tkinter import *
w=Tk()
w.geometry('600x600')
c1=StringVar()
c2=StringVar()
v1=StringVar()

def create():
    def create_add():
        name=c1.get()
        phn=c2.get()
        q=f"insert into phone (name,phonenumber) values (%s,%s)"
        mycursor.execute(q,[name,phn])
        mydb.commit()
        c1.set('')
        c2.set('')   

    Button(w,text="CREATE",bg="red",command=create).place(x=400,y=100)

    Button(w,text=" VIEW ",bg="red",command=view).place(x=600,y=100)

    Button(w,text="UPDATE",bg="red",command=update).place(x=800,y=100)

    Button(w,text="DELETE",bg="red").place(x=1000,y=100)

    f=Frame(w,bg="pink").place(x=500,y=200,height=400,width=500)
    l1=Label(f,text="Name :",font="Times 12",bg="pink").place(x=650,y=350)
    e1=Entry(f,textvariable=c1).place(x=700,y=350)
    l2=Label(f,text="Phone number :",font="Times 12",bg="pink").place(x=600,y=400)
    e2=Entry(f,textvariable=c2).place(x=700,y=400)
    Button(f,text="SUBMIT",bg="blue",command=create_add).place(x=700,y=450)
    
   

def view():
    def view_data():
        name = v1.get()
        query = "SELECT * FROM phone WHERE name = %s"
        mycursor.execute(query, (name,))
        res = mycursor.fetchone()
        v1.set('')
        
        if res:
            l_name = Label(f, text="Name: " + res[0], bg="pink",font="Times 14").place(x=720, y=400)
            l_phone = Label(f, text="Phone: " + str(res[1]),  bg="pink",font="Times 14").place(x=720, y=450)
        else:
            l_not_found = Label(f, text="Name not found!",  bg="pink").place(x=720, y=400)
    
    Button(w,text="CREATE",bg="red",command=create).place(x=400,y=100)

    Button(w,text=" VIEW ",bg="red",command=view).place(x=600,y=100)

    Button(w,text="UPDATE",bg="red",command=update).place(x=800,y=100)

    Button(w,text="DELETE",bg="red",command=delete).place(x=1000,y=100)

    f=Frame(w,bg="pink").place(x=500,y=200,height=400,width=500)
    l3=Label(f,text="Name :",font="Times 12",bg="pink").place(x=650,y=350)
    e3=Entry(f,textvariable=v1).place(x=700,y=350)
    Button(f,text="SEARCH",bg="blue",command=view_data).place(x=830,y=350)

def update():
    def update_work():
        name=c1.get()
        new_phone = c2.get()
        query = "UPDATE phone SET phonenumber = %s WHERE name = %s"
        mycursor.execute(query,[new_phone,name])
        mydb.commit()
        v1.set('')
        c1.set('')
        c2.set('')

    def updated():
        name = v1.get()
        query = "SELECT * FROM phone WHERE name = %s"
        mycursor.execute(query, (name,))
        res = mycursor.fetchone()


        if res:
            name = Label(f, text="Name: ", font="Times 12", bg="pink").place(x=700, y=400)
            name = Entry(f, textvariable=c1).place(x=750, y=400)
            phon = Label(f, text="Phone number: ", font="Times 12", bg="pink").place(x=650, y=450)
            phn = Entry(f, textvariable=c2).place(x=750, y=450)
            c1.set(res[0])
            c2.set(res[1])  
            Button(f, text="UPDATE", bg="blue", command=update_work).place(x=720, y=500)
        else:
            l_not_found = Label(f, text="Name not found!", font="Times 12", bg="pink").place(x=720, y=400)

    


    Button(w,text="CREATE",bg="red",command=create).place(x=400,y=100)

    Button(w,text=" VIEW ",bg="red",command=view).place(x=600,y=100)

    Button(w,text="UPDATE",bg="red",command=update).place(x=800,y=100)

    Button(w,text="DELETE",bg="red",command=delete).place(x=1000,y=100)

    f=Frame(w,bg="pink").place(x=500,y=200,height=400,width=500)
    l4=Label(f,text="Name :",font="Times 12",bg="pink").place(x=650,y=350)
    e4=Entry(f,textvariable=v1).place(x=700,y=350)
    Button(f,text="SEARCH",bg="blue",command=updated).place(x=830,y=350)

def delete():
    def delete_data():
        name= v1.get()
        query = "DELETE FROM phone WHERE name = %s"
        mycursor.execute(query, (name,))
        mydb.commit()
        v1.set('')
        
    Button(w,text="CREATE",bg="red",command=create).place(x=400,y=100)

    Button(w,text=" VIEW ",bg="red",command=view).place(x=600,y=100)

    Button(w,text="UPDATE",bg="red",command=update).place(x=800,y=100)

    Button(w,text="DELETE",bg="red",command=delete).place(x=1000,y=100)

    f=Frame(w,bg="pink").place(x=500,y=200,height=400,width=500)
    l3=Label(f,text="Name :",font="Times 12",bg="pink").place(x=650,y=350)
    e3=Entry(f,textvariable=v1).place(x=700,y=350)
    # Button(f,text="SEARCH",bg="blue",command=view).place(x=830,y=350)
    Button(f,text="DELETE",bg="blue",command=delete_data).place(x=750,y=400)
    


Button(w,text="CREATE",bg="red",command=create).place(x=400,y=100)

Button(w,text=" VIEW ",bg="red",command=view).place(x=600,y=100)

Button(w,text="UPDATE",bg="red",command=update).place(x=800,y=100)

Button(w,text="DELETE",bg="red",command=delete).place(x=1000,y=100)
w.mainloop()