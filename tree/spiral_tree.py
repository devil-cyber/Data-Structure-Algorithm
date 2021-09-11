from tree import Tree
from collections import deque


def spiral(root):
    d = deque()
    d.append(root)
    reverse = False
    stack = []
    while len(d)!=0:
        n = len(d)
        for i in range(n):
            curr = d.popleft()
            if reverse:
                stack.append(curr.data)
            else:
                print(curr.data,end=" ")
            if curr.left is not None:
                d.append(curr.left)
            if curr.right is not None:
                d.append(curr.right)
        if reverse:
            while len(stack)!=0:
                key = stack.pop()
                print(key,end=" ")
                
        print()
        reverse = not reverse


        
            

            
        
        

if __name__ == "__main__":
    t = Tree()
    root = t.create_tree()
    print('spiral transversal of tree:')
    spiral(root)
    print()

