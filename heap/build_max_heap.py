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

if __name__ == "__main__":
    arr = [10,15,50,4,20]
    buildMaxHeap(arr)
    print(arr)
