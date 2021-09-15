import heapq as h


def closest(arr, k, key):
    newarr = []
    n = len(arr)
    for i in range(n):
        newarr.append((abs(arr[i]-key),arr[i]))
    h.heapify(newarr)
    result = h.nsmallest(k, newarr)
    for i in result:
        print(i[1],end=" ")
    print()
    

if __name__ == "__main__":
    arr = [20,40,5,100,150]
    closest(arr,3,100)