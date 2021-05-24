from tkinter import Entry, Button, Tk, RIDGE, END

calculator = Tk()
calculator.title("calculator")

info_Tf = Entry(calculator, bd=30, insertwidth=4, relief=RIDGE, bg="peach puff")
info_Tf.grid(columnspan=10)

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
    expression = info_Tf.get()
    if not expression == '':
        result = eval(expression)
        info_Tf.delete(0, END)
        info_Tf.insert(END, result)
    else:
        info_Tf.insert(END, 'ERROR')
        print('Empty Expression!')
    
buttons = {
    '1': (one, 1, 0),
    '2': (two, 1, 2),
    '3': (three, 1, 3),
    '+': (add, 1, 4),
    '4': (four, 2, 0),
    '5': (five, 2, 2),
    '6': (six, 2, 3),
    '-': (sub, 2, 4),
    '7': (seven, 3, 0),
    '8': (eight, 3, 2),
    '9': (nine, 3, 3),
    '*': (mul, 3, 4),
    '.': (decimal, 4, 0),
    '0': (zero, 4, 2),
    '/': (div, 4, 3),
    'C': (changeback, 4, 4)

}

for key, value in buttons.items():
    action, row, col = value #(one, 1, 0)
    Button(calculator, bg="peach puff", padx=20, pady=20,fg="black", text=key, command=action).grid(row=row, column=col)

equalto = Button(calculator, bg="peach puff", padx=105, pady=20,text='=', command=calculate).grid(columnspan=5)

if __name__ == '__main__':
    calculator.mainloop()
