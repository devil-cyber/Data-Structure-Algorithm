import math
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

if __name__ == "__main__":
    arr = [10,15,50,4,20]
    buildMinHeap(arr)
    print(arr)
