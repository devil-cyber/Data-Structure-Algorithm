from tree import Tree
from collections import deque
import sys

def _max_width(root):
    if root is None:
        return None
    d = deque()
    d.append(root)
    maxwidth = -sys.maxsize
    while len(d)!=0:
        n = len(d)
        maxwidth = max(maxwidth,n)
        for i in range(n):
            curr = d.popleft()
            if curr.left is not None:
                d.append(curr.left)
            if curr.right is not None:
                d.append(curr.right)
    return maxwidth




if __name__ == "__main__":
    t = Tree()
    root = t.create_tree()
    print('The maximum width of the tree is:',_max_width(root))
    
