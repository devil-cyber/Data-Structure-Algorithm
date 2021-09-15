import heapq as heap


def kSorted(k, arr):
    n = len(arr)
    newarr = arr[:k+1]
    heap.heapify(newarr)
    target_index = 0
    for i in range(k+1,n):
        arr[target_index] = heap.heappop(newarr)
        heap.heappush(newarr, arr[i])
        target_index += 1
    # print(newarr, arr)
    while newarr:
        arr[target_index] = heap.heappop(newarr)
        target_index += 1
    return arr


if __name__ == "__main__":
    arr = [6,5,3,2,8,10,9]
    print(kSorted(3, arr))