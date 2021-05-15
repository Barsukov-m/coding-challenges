# Quicksort algorithm
# by Michael Barsukov

from random import randint


def partition_last(A, low, high): ...
def partition_first(A, low, high): ...
def partition_middle(A, low, high): ...


def quicksort(A, low, high):
    if low < high:
        # partition index
        # pi = partition_last(A, low, high)
        # pi = partition_first(A, low, high)
        pi = partition_middle(A, low, high)
        # A[pi] is now placed correctly

        quicksort(A, low, pi-1)
        quicksort(A, pi+1, high)


def partition_last(A, low, high):
    """
    This function returns the index of the correctly placed
    element. The last element is being selected as a pivot.
    """
    pivot = A[high]
    i = low-1
    for j in range(low, high):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[high], A[i+1] = A[i+1], A[high]
    return i+1


def partition_first(A, low, high):
    """
    This function returns the index of the correctly placed
    element. The first element is being selected as a pivot.
    """
    pivot = A[low]
    i = low
    for j in range(low+1, high+1):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[low], A[i] = A[i], A[low]
    return i


def partition_middle(A, low, high):
    """
    This function returns the index of the correctly placed
    element. The middle element is being selected as a pivot.
    """
    mid = low + (high-low) // 2  # middle element
    A[high], A[mid] = A[mid], A[high]
    pivot = A[high]
    i = low-1
    for j in range(low, high):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[high], A[i+1] = A[i+1], A[high]
    return i+1


if __name__ == '__main__':
    A = [randint(-100, 100) for i in range(10)]
    print(A)
    quicksort(A, 0, len(A)-1)
    print(A)
