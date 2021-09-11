from collections import deque

class Node:
    def __init__(self, data) -> None:
        self.right = None
        self.left = None
        self.data = data

class Tree:
    def __init__(self):
        pass

    def create_tree(self):
        root = Node(10)
        root.left = Node(20)
        root.right = Node(30)
        root.left.left = Node(40)
        root.left.right = Node(50)
        root.right.left = Node(60)
        root.right.left.left = Node(0)
        return root
"""
Tree
                10
              /   \
            20     30
           /  \   /
          40   50 60
                 /
                0
"""
        

"""
Print tree 1. inorder 2. preorder 3. postorder
inorder left -> root -> right
preorder root -> left -> right
postorder left -> right -> root
"""
def inorder(root) -> None:
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def height(root) -> int:
    if root is None:
        return 0
    return 1 + max(height(root.left),height(root.right))

# print all the node at (k+1)th level
def node_at_k(root, k):
    if root is None:
        return
    if k==0:
        print(root.data, end = " ")
    node_at_k(root.left, k - 1)
    node_at_k(root.right, k -1)
    
def level_order_transverasl(root):
    d = deque()
    d.append(root)
    while(len(d)!=0):
        curr = d.popleft()
        print(curr.data, end=" ")

        if curr.left is not None:
            d.append(curr.left)
        if curr.right is not None:
            d.append(curr.right)
    



if __name__ == '__main__':
    k = 2
    tree = Tree()
    root = tree.create_tree()
    print('Tree inorder transversal:',end=" ")
    inorder(root)
    print()
    print('The height of tree:', height(root))
    print(f'Node at distance {k} from root:',end=" ")
    node_at_k(root, k)
    print()
    print('Level order transversal of tree: ',end=" ")
    level_order_transverasl(root)
    print()

