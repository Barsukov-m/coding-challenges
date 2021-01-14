from tkinter import *


class CalcButton:
    def __init__(self, master, size, text):
        self.button = Button(master, text=text,
                             padx=(25*size), pady=20,bd=3,
                             command=self.push)
        self.text = text
        
    def push(self):
        data = problem.get()
        problem.delete(0, END)
        problem.insert(0, data + self.text)


def reset():
    problem.delete(0, END)

def evaluate(n1, n2, s):
    if s == '+':
        return int(n1) + int(n2)
    elif s == '-':
        return int(n1) - int(n2)
    elif s == '*':
        return int(n1) * int(n2)
    elif s == '/':
        return int(n1) / int(n2)

def solve():
    s = problem.get() 
    # First result is formed by adding 0 to the first operand
    operand_1, operand_2 = '0', ''
    operator = '+'
    negative = 0 # Negative number state
    
    # Reading the entry data
    i = 0
    while s: # Entry data is not empty
        while True: # Reading the sign
            if s[i].isdigit() or s[i] in ' +-*/':
                if s[i] == '+':
                    i += 1
                    continue
                elif s[i] == '-':
                    # Inverse the negative number state
                    negative = not negative
                elif s[i].isdigit():
                    if negative:
                        operand_2 = '-' + operand_2
                    operand_2 += s[i]
                    i += 1
                    break
            i += 1
        
        while i < len(s): # Reading the number
            if s[i].isdigit() or s[i] in ' +-*/':
                if s[i].isdigit():
                    operand_2 += s[i]
                elif s[i] in '+-*/':
                    operand_1 = evaluate(operand_1, operand_2, operator)
                    operator = s[i]
                    negative = 0
                    operand_2 = ''
                    i += 1
                    break
            i += 1
        if i >= len(s):
            operand_1 = evaluate(operand_1, operand_2, operator)
            break
        
    problem.delete(0, END)
    problem.insert(0, operand_1)
    

root = Tk()
root.title('Calculator')
# root.minsize(400, 500)
root.maxsize(400, 500)

container = Label(root)
# container.grid(row=0, column=0, expand=1, fill=X)
container.pack(pady=50, expand=1, fill=Y)

# Initialize program content
problem = Entry(container, width=35)

btn_1 = CalcButton(container, 1, '1')
btn_2 = CalcButton(container, 1, '2')
btn_3 = CalcButton(container, 1, '3')
btn_4 = CalcButton(container, 1, '4')
btn_5 = CalcButton(container, 1, '5')
btn_6 = CalcButton(container, 1, '6')
btn_7 = CalcButton(container, 1, '7')
btn_8 = CalcButton(container, 1, '8')
btn_9 = CalcButton(container, 1, '9')
btn_0 = CalcButton(container, 1, '0')
btn_eval = CalcButton(container, 2, '=')
btn_eval.button['command'] = solve

btn_add = CalcButton(container, 1, '+')
btn_sub = CalcButton(container, 1, '-')
btn_prod = CalcButton(container, 1, '*')
btn_div = CalcButton(container, 1, '/')

btn_reset = Button(container, text="Reset", bd=3,
                   command=reset)

# Place the content on the screen
problem.grid(row=0, column=0, columnspan=4, pady=20)

btn_7.button.grid(row=1, column=0)
btn_8.button.grid(row=1, column=1)
btn_9.button.grid(row=1, column=2)
btn_div.button.grid(row=1, column=3)

btn_4.button.grid(row=2, column=0)
btn_5.button.grid(row=2, column=1)
btn_6.button.grid(row=2, column=2)
btn_prod.button.grid(row=2, column=3)

btn_1.button.grid(row=3, column=0)
btn_2.button.grid(row=3, column=1)
btn_3.button.grid(row=3, column=2)
btn_sub.button.grid(row=3, column=3)

btn_0.button.grid(row=4, column=0)
btn_eval.button.grid(row=4, column=1, columnspan=2)
btn_add.button.grid(row=4, column=3)

btn_reset.grid(row=5, column=0, columnspan=4)


root.mainloop()