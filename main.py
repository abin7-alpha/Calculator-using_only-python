from tkinter import Entry, Button, Tk, RIDGE, END

calculator = Tk()
calculator.title("calculator")

info_Tf = Entry(calculator, bd=30, insertwidth=4, relief=RIDGE, bg="peach puff")
info_Tf.grid(columnspan=10)

# A function that either accepts or returns another function is called higher order function
def create_action(entry, char, pos):

    def action():
        entry.insert(pos, char)

    return action

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
    '1': (1, 0),
    '2': (1, 2),
    '3': (1, 3),
    '+': (1, 4),
    '4': (2, 0),
    '5': (2, 2),
    '6': (2, 3),
    '-': (2, 4),
    '7': (3, 0),
    '8': (3, 2),
    '9': (3, 3),
    '*': (3, 4),
    '.': (4, 0),
    '0': (4, 2),
    '/': (4, 3),
    'C': (4, 4)
}

def create_buttons(buttons):
    for key, value in buttons.items():
        row, col = value

        # Create corresponding action
        if key == 'C':
            action = lambda : info_Tf.delete(0, END)
        else:
            action = create_action(info_Tf, key, END) 
        
        # Create an instance/object of a button
        Button(
            calculator, 
            bg="peach puff", 
            padx=20, 
            pady=20, 
            fg="black", 
            text=key, 
            command=action
        ).grid(row=row, column=col)

create_buttons(buttons)

equalto = Button(
            calculator, 
            bg="peach puff", 
            padx=105, 
            pady=20,
            text='=', 
            command=calculate
          ).grid(columnspan=5)

if __name__ == '__main__':
    calculator.mainloop()
