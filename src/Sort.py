import sys
import random
import time

def report():
    print("Random Array:")
    x = generateArray()
    # print(x, "\n", "length:", len(x))

    selectTime = selectionSort(x, len(x))
    print("time to complete: ", selectTime)

    bubbleTime = bubbleSort()
    mergeTime = mergeSort()
    quickTime = quickSort()

def generateArray():
    array= []
    for x in range(0, 1000):
        array.append(random.randint(-999,999))
    return array

def selectionSort(A, n):
    start = time.time()
    i = 0
    while i < n-1:
        first = i
        minimum = first
        j = i+1
        while j < n:
            if A[j] < A[minimum]:
                minimum = j
            j+=1
        if minimum is not first:
            temp = A[minimum]
            A[minimum] = A[i]
            A[i] = temp
        i+=1
    end = time.time()
    MILLI = 1000
    duration = (end-start)*MILLI
    return duration

def bubbleSort():
    return 0

def mergeSort():
    return 0

def merge():
    return 0

def quickSort():
    return 0

def partition():
    return 0


report()