from min_heap import Min_Heap

def Heapify(mh, i):
    l = mh.left(i)
    r = mh.right(i)
    arr = mh.arr
    size = mh.size
    smallest = i
    if (l < size) and (arr[l] < arr[i]):
        smallest = l
    if (r < size) and (arr[r] < arr[smallest]):
        smallest = r
    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        Heapify(mh, smallest)



if __name__ == "__main__":
    mh = Min_Heap()
    mh.create_heap()
    print(mh.arr)
    Heapify(mh, 0)
    Heapify(mh, 0)
    Heapify(mh, 0)
    print(mh.arr)
