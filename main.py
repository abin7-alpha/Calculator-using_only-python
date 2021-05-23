from tkinter import *

ws = Tk()
ws.title("calculator")

info_Tf = Entry(ws, bd=30, insertwidth=4, relief=RIDGE, bg="peach puff")
info_Tf.insert(END, '')
info_Tf.grid(columnspan=5)

def add():
    info_Tf.insert(END, '+')
def sub():
    info_Tf.insert(END, '-')
def div():
    info_Tf.insert(END, '/')

def mul():
    info_Tf.insert(END, '*') 
def one():
    info_Tf.insert(END, '1')
def two():
    info_Tf.insert(END, '2')
def three():
    info_Tf.insert(END, '3')     
def four():
    info_Tf.insert(END, '4')
def five():
    info_Tf.insert(END, '5')  
def six():
    info_Tf.insert(END, '6')  
def seven():
    info_Tf.insert(END, '7')  
def eight():
    info_Tf.insert(END, '8')
def nine():
    info_Tf.insert(END, '9')   
def zero():
    info_Tf.insert(END, '0')   
def decimal():
    info_Tf.insert(END, '.')    

def changeback():
    info_Tf.delete(0, END)  

def calculate():
    current_values = info_Tf.get()
    summation = str(eval(current_values))
    info_Tf.delete(0, END)
    info_Tf.insert(END, summation)
    
b1 = Button(ws, bg="peach puff", padx=20, pady=20,fg="black", text='1', justify= "left", command= one).grid(row=1, column=0)
b2 = Button(ws, bg="peach puff", padx=20, pady=20,fg="black", text='2', command=two).grid(row=1, column=2)
b3 = Button(ws, bg="peach puff", padx=20, pady=20,fg="black", text='3', command=three).grid(row=1, column=3)
adds = Button(ws, bg="peach puff", padx=20, pady=20,fg="black", text='+', command=add).grid(row=1, column=4)
b4 = Button(ws, bg="peach puff", padx=20, pady=20,fg="black", text='4', justify= "left", command= four).grid(row=2, column=0)
b5 = Button(ws, bg="peach puff", padx=20, pady=20,fg="black", text='5', command=five).grid(row=2, column=2)
b6 = Button(ws, bg="peach puff", padx=20, pady=20,fg="black", text='6', command=six).grid(row=2, column=3)
subs = Button(ws, bg="peach puff", padx=20, pady=20,fg="black", text='-', command=sub).grid(row=2, column=4)
b7 = Button(ws, bg="peach puff", padx=20, pady=20,fg="black", text='7', justify= "left", command= seven).grid(row=3, column=0)
b8 = Button(ws, bg="peach puff", padx=20, pady=20,fg="black", text='8', command=eight).grid(row=3, column=2)
b9 = Button(ws, bg="peach puff", padx=20, pady=20,fg="black", text='9', command=nine).grid(row=3, column=3)
multi = Button(ws, bg="peach puff", padx=20, pady=20,fg="black", text='*', command=mul).grid(row=3, column=4)
decm = Button(ws, bg="peach puff", padx=20, pady=20,fg="black", text='.', justify= "left", command= decimal).grid(row=4, column=0)
zer = Button(ws, bg="peach puff", padx=20, pady=20,fg="black", text='0', command=zero).grid(row=4, column=2)
divs = Button(ws, bg="peach puff", padx=20, pady=20,fg="black", text='/', command=div).grid(row=4, column=3)
cnbc = Button(ws, bg="peach puff", padx=20, pady=20,fg="black", text='c', command=changeback).grid(row=4, column=4)
equalto = Button(ws, bg="peach puff", padx=105, pady=20,text='=', command=calculate).grid(columnspan=5)

if __name__ == '__main__':
    ws.mainloop()