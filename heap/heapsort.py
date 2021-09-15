import math
def maxheapify(i, n, arr):
    largest = i
    left = 2*i +1
    right = 2*i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxheapify(largest, n, arr)
def buildMaxHeap(arr):
    n = len(arr)
    index = math.floor((n-1)/2)
    for i in range(index,-1,-1):
        maxheapify(i, n, arr)

def minheapify(i, n, arr):
    smallest = i
    left = 2*i +1
    right = 2*i + 2
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        minheapify(smallest, n, arr)
def buildMinHeap(arr):
    n = len(arr)
    index = math.floor((n-1)/2)
    for i in range(index,-1,-1):
        minheapify(i, n, arr)

def heapSort(arr, reverse = False):
    if not reverse:
        buildMaxHeap(arr)
        n = len(arr)
        for i in range(n-1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            maxheapify(0, i, arr)
        return arr
    else:
        buildMinHeap(arr)
        n = len(arr)
        for i in range(n-1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            minheapify(0, i, arr)
        return arr



if __name__ == "__main__":
    # for decreasing order try reverse == True in heapsort
    arr = [10,15,50,4,20]
    newarr = heapSort(arr, reverse=True)
    print(newarr)
