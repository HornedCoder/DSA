 
def bubbleSort(cList):
    for i in range(len(cList)-1):
        for j in range(len(cList)-i-1):
            if cList[j] > cList[j+1]:
                cList[j], cList[j+1] = cList[j+1], cList[j]
    print(cList)

#cList = [3,2,1,4,5]
#bubbleSort(cList)


def selectionSort(cList):
    for i in range(len(cList)):
        minIndex = i
        for j in range(i+1, len(cList)):
            if cList[j] < cList[minIndex]:
                minIndex = j
        cList[i], cList[minIndex] = cList[minIndex], cList[i]
    print(cList)


def insertionSort(cList):
    for i in range(1,len(cList)):
        key = cList[i]
        j = i-1
        while j >= 0 and key < cList[j]:
            cList[j+1] = cList[j]
            j -= 1
        cList[j+1] = key
    print(cList)

def merge(cList, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = cList[l+i]

    for j in range(0, n2):
        R[j] = cList[m+1+j]

    i, j = 0, 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            cList[k] = L[i]
            i += 1
        else:
            cList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        cList[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        cList[k] = R[j]
        j += 1
        k += 1

def mergeSort(cList, l, r):
    if l < r:
        m = (l+(r-1)) // 2
        mergeSort(cList, l, m)
        mergeSort(cList, m+1, r)
        merge(cList, l, m, r)
    return cList


def swap(cList, index1, index2):
    cList[index1], cList[index2] = cList[index2], cList[index1]

def pivot(cList, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index + 1):
        if cList[i] < cList[pivot_index]:
            swap_index += 1
            swap(cList, swap_index, i)
    swap(cList, pivot_index, swap_index)
    return swap_index

def quickSort(cList, left, right):
    if left < right:
        pivot_index = pivot(cList, left, right)
        quickSort(cList, left, pivot_index-1)
        quickSort(cList, pivot_index+1, right)
    return cList
    
def heapify(arr, n, i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and arr[left] > arr[largest]:
        largest = left
        
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]

        heapify(arr, i, 0)


arr = [11,13,12,7,8,6]
heap_sort(arr)
print(arr)

