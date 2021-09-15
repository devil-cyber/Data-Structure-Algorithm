import heapq

arr = [10,15,50,4,20]
heapq.heapify(arr)
print(arr)
print(heapq.heappop(arr))
print(heapq.nlargest(1, arr))