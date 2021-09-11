from tree import Tree



prev = None
def tree_to_linkedlist(root):
    global prev
    if root is None:
        return 
    head = tree_to_linkedlist(root.left)
    if prev == None:
        head = root
    else:
        root.left = prev
        prev.right = root
    prev = root
    tree_to_linkedlist(root.right)
    return head

if __name__ == "__main__":
    t = Tree()
    root = t.create_tree()
    print('Tree to doubly linked list: ')
    head = tree_to_linkedlist(root)
    print(head.data)

    

        