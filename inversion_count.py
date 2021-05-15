# Insertion Count Using Merge Sort
# by Michael Barsukov

def merge(A, left, mid, right):
    i = left     # left array pointer
    j = mid+1    # right array pointer
    inv_sum = 0  # inversion counter
    A_tmp = []   # temporary array

    # while left and right halves are not empty
    while i <= mid and j <= right:
        if A[i] > A[j]:  # inversion was found
            A_tmp.append(A[j])
            inv_sum += mid-i+1
            j += 1
        else:
            A_tmp.append(A[i])
            i += 1

    while i <= mid:         # left array is not empty
        A_tmp.append(A[i])  # add remaining elements
        i += 1
    while j <= right:       # right array is not empty
        A_tmp.append(A[j])  # add remaining elements
        j += 1

    for i in range(left, right+1):  # copy A_tmp data
        A[i] = A_tmp[i-left]

    return inv_sum


def inversion_count(A, left, right):
    """
    Recursive implementation of merge sort and insertion
    count.
    """
    if left >= right:
        return 0

    inv_sum = 0
    mid = left + (right-left)//2
    inv_sum += inversion_count(A, left, mid)
    inv_sum += inversion_count(A, mid+1, right)
    return inv_sum + merge(A, left, mid, right)


if __name__ == '__main__':
    A = [13, 7, 8, 7, 1, 5]
    print(A)
    inversions = inversion_count(A, 0, len(A)-1)
    print('%d inversions in total.' % inversions)
