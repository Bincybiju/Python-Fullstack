from tkinter import *
w = Tk()

display = StringVar()

def button_click(t):
    current = entry.get()
    if current in ['0','+','*','/']:
        entry.delete(0, END)
        entry.insert(0,current[:-1]+t)
    else: 
        entry.delete(0, END)
        entry.insert(0,current+t)

def button_clear():
    entry.delete(0, END)

def back():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current[:-1])

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

entry = Entry(w, width=20, font=('Arial', 20), textvariable=display)
entry.grid(row=0, column=0, columnspan=4)
b=Button(w,text=7,command=lambda t:button_click(7))
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('D', 4, 1), ('.', 4, 2), ('+', 4, 3)
]
b=Button(w,text=7,command=lambda t:button_click(7))
for (text, row, col) in buttons:
    button = Button(w, text=text, padx=20, pady=20, font=('Arial', 16),
                    command=lambda t=text: button_equal() if t == '=' else back() if t == "D" else button_click(t))
    button.grid(row=row, column=col)

b_r = Button(w, text=' = ', bg="red", foreground='white', font=('Arial', 16), command=button_equal).grid(row=5,column=0,columnspan=2,ipadx=50)
b_b = Button(w, text=' C ', foreground='white', bg="red", font=('Arial', 16),command=button_clear).grid(row=5,column=2,columnspan=2,ipadx=50)

w.mainloop()
