import sys
import random
import time
import copy

def generateArray(size):
    array = []
    i = 0
    for i in range(0, size):
        #TODO: Change back to (-999, 999)
        array.append(random.randint(-9, 9))
    print(array, "\n")
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
        if minimum is not first:
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
    #TODO: Merge Sort Algorithm

    end = time.time()
    MILLI = 1000
    duration = (end - start)*MILLI
    return duration

def merge(A, low, mid, high):
    '''
    Merge Sort part 2: Merges the two arrays together into one array.
    '''
    b = generateArray(mid - low + 1)
    c = generateArray(high - mid)

    #TODO: Merge arrays


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
    while j < (high-1) or j is (high-1):
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
    print("Random Array:")
    SIZE = 10
    arr = generateArray(SIZE)

    # Must create shallow copies of `arr` since I want modify values in the new array without changing the old one.
    forSS = copy.copy(arr)
    forBS = copy.copy(arr)
    forMS = copy.copy(arr)
    forQS = copy.copy(arr)

    print("BEFORE SORTING")
    print("SS: ", forSS)
    print("BS: ", forBS)
    print("MS: ", forMS)
    print("QS: ", forQS)

    selectTime = selectionSort(forSS, len(forSS))
    print("-------------------------------")
    print("AFTER SELECTION SORT")

    print("SS: ", forSS)
    print("BS: ", forBS)
    print("MS: ", forMS)
    print("QS: ", forQS)

    
    bubbleTime = bubbleSort(forBS, len(forBS))
    print("-------------------------------")
    print("AFTER BUBBLE SORT")

    print("SS: ", forSS)
    print("BS: ", forBS)
    print("MS: ", forMS)
    print("QS: ", forQS)

    mergeTime = mergeSort(forMS, 0, (len(forMS)-1))
    print("-------------------------------")
    print("AFTER MERGE SORT")

    print("SS: ", forSS)
    print("BS: ", forBS)
    print("MS: ", forMS)
    print("QS: ", forQS)

    quickTime = quickSort(forQS, 0, (len(forQS)-1))
    print("-------------------------------")
    print("AFTER QUICK SORT")

    print("SS: ", forSS)
    print("BS: ", forBS)
    print("MS: ", forMS)
    print("QS: ", forQS)
   

    # print("-------------------------------")
    # print("New order using Selection Sort:")
    # print(forSS)
    # print("Time to complete: ", selectTime, "Milliseconds")
    # #TODO: Count code lines for Selection Sort Algorithm
    # print("Total lines of code: ???")
    # print("")

    # print("-------------------------------")
    # print("New order using Bubble Sort:")
    # print(forBS)
    # print("Time to complete: ", bubbleTime, "Milliseconds")
    # #TODO: Count code lines for Bubble Sort Algorithm
    # print("Total lines of code: ???")
    # print("")

    # print("-------------------------------")
    # print("New order using Merge Sort:")
    # print(forMS)
    # print("Time to complete: ", mergeTime, "Milliseconds")
    # #TODO: Count code lines for Merge Sort Algorithm
    # print("Total lines of code: ???")
    # print("")

    # print("-------------------------------")
    # print("New order using Quick Sort:")
    # print(forQS)
    # print("Time to complete: ", quickTime, "Milliseconds")
    # #TODO: Count code lines for Quick Sort Algorithm
    # print("Total lines of code: ???")
    # print("")

report()