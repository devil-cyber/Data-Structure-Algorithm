## There is some eror in problem
import heapq as h


def MedianStream(arr):
    s = []
    g = []
    n = len(arr)
    h.heappush(s,arr[0])
    print(s[0])
    for i in range(1, n):
        x = arr[i]
        if len(s) > len(g):
            if max(s)>x:
                sdata = s.pop()
                h.heapify(s)
                h.heappush(g,sdata)
                h.heappush(s,x)
            else:
                h.heappush(g,x)
                print((max(s)+max(g))/2)
        else:
            if x <= max(s):
                h.heappush(s,x)
            else:
                h.heappush(g,x)
                gdata = h.heappop(g)
                h.heappush(s,gdata)
                print(max(s))



if __name__ == "__main__":
    arr = [12,15,10,5,8,7,16]
    MedianStream(arr)
