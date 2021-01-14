# Determinant solver

def minor(A, n, m):
    try:  # Correct function call test
        A[n][m]
    except IndexError:
        return []

    mi = []  # Minor array
    for i in range(len(A)):
        mi += [[]]  # Add a row
        for j in range(len(A[0])):
            if i != n and j != m:
                mi[i].append(A[i][j])
    while [] in mi:  # Remove empty rows
        del mi[mi.index([])]
    return mi


def mdeterm(A):
    if len(A) == 1 and len(A[0]) == 1:
        return A[0][0]
    if len(A) != len(A[0]):  # Not a square matrix
        return None

    d = 0
    for i in range(len(A)):  # Solving by row recursively
        d += (-1)**i * A[0][i]*mdeterm(minor(A, 0, i))
    return d


M = [[5, 9, 1],
     [4, -1, 5],
     [5, 0, 3]]

while True:
    try:
        size = int(input('Number of rows: '))
        break
    except TypeError:
        print('Please enter a valid decimal number.')

A = []
for i in range(size):
    col = input("Col1 (separate by ' '): ").split()
    try:
        for i in range(len(col)):
            col[i] = str(col[i])
    except Exception:
        print('Please enter valid numbers.')
        break
    A += col

print('\nDETERMINANT:', mdeterm(A))
