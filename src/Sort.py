import sys
import random
import time
import copy

def generateArray(size):
    array = []
    i = 0
    for i in range(0, size):
        array.append(random.randint(-999, 999))
    return array

def selectionSort(A, n):
    start = time.time()
    i = 0
    while i < (n - 1):
        first = i
        minimum = first
        j = i + 1
        while j < n:
            if A[j] < A[minimum]:
                minimum = j
            j += 1
        if not(minimum == first):
            temp = A[minimum]
            A[minimum] = A[i]
            A[i] = temp
        i += 1
    end = time.time()
    MILLI = 1000
    duration = (end - start)*MILLI
    return duration

def bubbleSort(A, n):
    start = time.time()
    i = 0
    while i < n:
        j = 1
        while j < (n - i):
            if A[j - 1] > A[j]:
                temp = A[j - 1]
                A[j-1] = A[j]
                A[j] = temp
            j += 1
        i += 1
    end = time.time()
    MILLI = 1000
    duration = (end - start)*MILLI
    return duration

def mergeSort(A, low, high):
    start = time.time()
    if low < high:
        middle = int((low + high)/2)
        mergeSort(A, low, middle)
        mergeSort(A, middle+1, high)
        merge(A, low, middle, high)
    end = time.time()
    MILLI = 1000
    duration = (end - start)*MILLI
    return duration

def merge(A, low, mid, high):
    '''
    Merge Sort part 2: Merges the two arrays together into one array.
    '''
    b = generateArray((mid - low) + 1)
    c = generateArray(high - mid)
    i = 0
    while i < len(b):
        b[i] = A[low + i]
        i += 1
    j = 0
    while j < len(c):
        c[j] = A[(mid + 1) + j]
        j += 1

    k = low
    i = 0
    j = 0
    while i < len(b) and j < len(c):
        if b[i] < c[j]:
            A[k] = b[i]
            i += 1
            k += 1
        else:
            A[k] = c[j]
            j += 1
            k += 1

    if i == len(b):
        while j < len(c):
            A[k] = c[j]
            j += 1
            k += 1
    else:
        while i < len(b):
            A[k] = b[i]
            i += 1
            k += 1

def quickSort(A, low, high):
    start = time.time()
    if low > high:
        return 0
    else:
        i = partition(A, low, high)
        quickSort(A, low, i-1)
        quickSort(A, i+1, high)

    end = time.time()
    MILLI = 1000
    duration = (end - start)*MILLI
    return duration

def partition(A, low, high):
    pivot = A[high]
    i = low - 1
    j = low
    while j < (high-1) or j == (high-1):
        if A[j] <= pivot:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
        j += 1
    temp = A[i + 1]
    A[i + 1] = A[high]
    A[high] = temp
    return i + 1

def report():
    SIZE = 7800
    arr = generateArray(SIZE)
    #print("Random Array:", "\n", arr)
    # Must create shallow copies of `arr` since I want modify values in the new array without changing the old one.
    forSS = copy.copy(arr)
    forBS = copy.copy(arr)
    forMS = copy.copy(arr)
    forQS = copy.copy(arr)
    selectTime = selectionSort(forSS, len(forSS))    
    bubbleTime = bubbleSort(forBS, len(forBS))
    mergeTime = mergeSort(forMS, 0, (len(forMS)-1))
    quickTime = quickSort(forQS, 0, (len(forQS)-1))
    #TODO: Count code lines for each algorithm
    print("-------------------------------")
    print("New order using Selection Sort:")
    #print(forSS)
    print("Time to complete: ", selectTime, "Milliseconds")
    print("Total lines of code: 14")
    print("-------------------------------")
    print("New order using Bubble Sort:")
    #print(forBS)
    print("Time to complete: ", bubbleTime, "Milliseconds")
    print("Total lines of code: 10")
    print("-------------------------------")
    print("New order using Merge Sort:")
    #print(forMS)
    print("Time to complete: ", mergeTime, "Milliseconds")
    print("Total lines of code: 37")
    print("-------------------------------")
    print("New order using Quick Sort:")
    #print(forQS)
    print("Time to complete: ", quickTime, "Milliseconds")
    print("Total lines of code: 19")

report()