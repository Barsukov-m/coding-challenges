def merge(A, left, mid, right):
    A1 = A[left:mid+1]     # left half
    A2 = A[mid+1:right+1]  # right half
    Ai = left              # array pointer
    while A1 and A2:       # two arrays are not empty
        if A1[0] < A2[0]:  # compare first elements
            A[Ai] = A1[0]  # add smaller value to the initial array
            del A1[0]      # remove the value from the left half
        else:
            A[Ai] = A2[0]
            del A2[0]
        Ai += 1            # move the array pointer forward
    while A1:              # left half still not empty
        A[Ai] = A1[0]
        del A1[0]
        Ai += 1
    while A2:              # right half still not empty
        A[Ai] = A2[0]
        del A2[0]
        Ai += 1


def merge_sort(A, left, right):
    if left >= right:
        return
    mid = left + (right-left)//2
    merge_sort(A, left, mid)
    merge_sort(A, mid+1, right)
    merge(A, left, mid, right)    # merge left and right halves


if __name__ == '__main__':
    A = [1, 3, 5, 2, 4, 6]
    print(A)
    merge_sort(A, 0, len(A)-1)
    print(A)
