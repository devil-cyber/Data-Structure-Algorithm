# Buy itme with given price as list with bound to given price sum
import heapq as h

def buyItem(arr, _sum):
    h.heapify(arr)
    result = 0
    count = 0
    while result <= _sum:
        key = h.heappop(arr)
        result += key
        count += 1
        h.heapify(arr)
    return count - 1

if __name__ == "__main__":
    arr = [20,10,5,30,100]
    print(buyItem(arr,35))