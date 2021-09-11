class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def search(ino, start, end,root):
    for i in range(start, end+1):
        if root.data == ino[i]:
            return i

def Tree(pre, ino, start, end):
    if start > end:
        return None
    root = Node(pre[Tree.preindex])
    Tree.preindex += 1
    index = search(ino,start,end,root)
    root.left = Tree(pre, ino,start, index-1)
    root.right = Tree(pre, ino, index+1, end)
    return root

def inorder(root) -> None:
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)





if __name__ == "__main__":
    pre = [10, 20, 40, 50, 30, 60, 0]
    ino = [40, 20, 50, 10, 0, 60, 30]
    Tree.preindex = 0
    root = Tree(pre, ino,0, len(pre)-1)
    # test the new tree by printing inorder
    inorder(root)
    print()
