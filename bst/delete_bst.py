from bst import BST

"""
To delete a node from a Binary Search There are three posibilities:
1.Node to be deleted is a leaf node.
2.Node to be deleted has only one child.
3.Node to be deleted has two children.
"""

def get_successor(root):
    node = root.right
    while node!=None and node.left!=None:
        node = node.left
    return node

def delete(root, key):
    if root is None:
        return root
    if key > root.data:
        root.right = delete(root.right, key)
    elif key < root.data:
        root.left = delete(root.left, key)
    else:
        if root.right == None:
            temp = root.left
            root = None
            return temp
        elif root.left is None:
            temp = root.right 
            root = None
            return temp
        else:
            temp = get_successor(root)
            root.data = temp.data
            root.right = delete(root.right, temp.data)
    return root
# inorder transversal to check the function is deleting the node 
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

if __name__ == "__main__":
    b = BST()
    root = b.create_bst()
    print('Bst before deletion:',end=" ")
    inorder(root)
    print()
    delete(root,11)
    print('BST after deletion:',end=" ")
    inorder(root)
    print()