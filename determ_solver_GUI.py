from tkinter import *


class Cell:

    def __init__(self, master, x, y):
        self.cell = Entry(master, width=5)
        self.cell.grid(row=x, column=y)


def minor(A, n, m):
    try:  # Correct function call test
        A[n][m]
    except IndexError:
        return []

    M = []  # Minor array
    for i in range(len(A)):
        M += [[]]  # Add a row
        for j in range(len(A[0])):
            if i != n and j != m:
                M[i].append(A[i][j])
    while [] in M:  # Remove empty rows
        del M[M.index([])]
    return M


def mdeterm(A):
    if len(A) == 1 and len(A[0]) == 1:
        return A[0][0]
    if len(A) != len(A[0]):  # Not a square matrix
        return None

    d = 0
    for i in range(len(A)):  # Solving by row recursively
        d += (-1)**i * A[0][i]*mdeterm(minor(A, 0, i))
    return d


def determ(A):
    global determ_lbl
    M = []
    for i in range(len(A)):
        M += [[]]
        for j in range(len(A[0])):
            value = A[i][j].cell.get()
            try:
                M[i].append(int(value))
            except ValueError:
                M[i].append(0)
    try:  # Remove the previous answer
        determ_lbl.destroy()
    except NameError:
        pass

    determ_lbl = Label(text=mdeterm(M))
    if mdeterm(M) is None:
        determ_lbl.config(text='Not a square Matrix')
    determ_lbl.grid(row=1, column=1)


def rows(A, add=True):
    if add:
        A += [[]]
        for i in range(len(A[0])):
            A[-1].append(Cell(matrix, len(A), i+1))
    else:
        if len(A) <= 1:
            print(1)
            return
        for c in A[-1]:
            try:
                c.cell.destroy()
            except Exception as e:
                print(e)
        del A[-1]


def cols(A, add=True):
    if add:
        for i in range(len(A)):
            A[i].append(Cell(matrix, i+1, len(A[i])+1))
    else:
        if len(A[0]) <= 1:
            print(1)
            return
        for r in A:
            try:
                r[-1].cell.destroy()
                del r[-1]
            except Exception as e:
                print(r[-1])
                print(e)


root = Tk()
root.config(padx=20, pady=20)
matrix = Frame(root)

matrix.grid(row=0, column=0, rowspan=2, padx=20)

btn_add_row = Button(matrix, text='+', padx=6, pady=1,
                     command=lambda: rows(A))
btn_add_col = Button(matrix, text='+', padx=6, pady=1,
                     command=lambda: cols(A))
btn_rem_row = Button(matrix, text='-', padx=6, pady=1,
                     command=lambda: rows(A, False))
btn_rem_col = Button(matrix, text='-', padx=6, pady=1,
                     command=lambda: cols(A, False))

btn_add_row.grid(row=0, column=1)
btn_add_col.grid(row=1, column=0)
btn_rem_row.grid(row=0, column=2)
btn_rem_col.grid(row=2, column=0)

A = [[Cell(matrix, i, j) for j in range(1, 4)] for i in range(1, 4)]

determ_btn = Button(root, text='Determ', command=lambda: determ(A))
determ_btn.grid(row=0, column=1)

root.mainloop()
