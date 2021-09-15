import math as mat
class Min_Heap:
    def __init__(self) -> None:
        self.size = 0
        self.arr = []
    def left(self, i):
        return (2*i + 1)
    def right(self, i):
        return (2*i + 2)
    def parent(self, i):
        index = mat.floor((i-1)/2)
        return index
    def insert(self, data):
        self.size += 1
        self.arr.append(data)
        j = self.size -1
        for i in range(j, 0):
            if (self.arr[self.parent(i)]>self.arr[i]):
                self.arr[i], self.arr[self.parent(i)] = self.arr[i], self.arr[self.parent(i)]
                i = self.parent(i)
    def create_heap(self):
        self.insert(100)
        self.insert(20)
        self.insert(11)
        self.insert(17)
        self.insert(12)
        self.insert(8)
    
# if __name__ == "__main__":
#     mh = Min_Heap()
#     mh.insert(10)
#     mh.insert(11)
#     mh.insert(12)
#     mh.insert(5)
#     mh.insert(6)
#     mh.insert(100)
#     print(mh.arr)
