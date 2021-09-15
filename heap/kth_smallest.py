import heapq as heap

def kthSmallest(arr, k):
    heap.heapify(arr)
    newarr = heap.nsmallest(k, arr)
    return newarr[k-1]


if __name__ == '__main__':
    arr = [7,10,4,3,20,15]
    k = 3
    print(kthSmallest(arr, k))