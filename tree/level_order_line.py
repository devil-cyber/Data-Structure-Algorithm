from tree import Tree
from collections import deque


def __level_order_line__(root):
    d = deque()
    d.append(root)
    while len(d)!=0:
        n = len(d)
        for i in range(n):
            curr = d.popleft()
            print(curr.data,end=" ")
            if curr.left is not None:
                d.append(curr.left)
            if curr.right is not None:
                d.append(curr.right)
        print()
        

if __name__ == "__main__":
    t = Tree()
    root = t.create_tree()
    print('level order transversal of tree:')
    __level_order_line__(root)
    print()

