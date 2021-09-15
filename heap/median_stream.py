
import heapq as h


def median(arr):
    s = [] # max heap
    g = [] # min heap
    n = len(arr)
    h.heappush(s, -arr[0])
    print(arr[0])
    for i in range(1,n):
        x = arr[i]
        if len(s) > len(g):
            if (-s[0]) > x:
                sdata = -h.heappop(s)
                h.heappush(g, sdata)
                h.heappush(s,-x)
            else:
                h.heappush(g,x)
            print(((-s[0])+g[0])/2)
        else:
            if x <= (-s[0]):
                h.heappush(s, -x)
            else:
                h.heappush(g, x)
                gdata = h.heappop(g)
                h.heappush(s, -gdata)
            print(-s[0])



if __name__ == "__main__":
    arr = [12,15,10,5,8,7,16]
    median(arr)
