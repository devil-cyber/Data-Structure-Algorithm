from tree import Tree

number_node = 100
visited = [False] * number_node

def left_view(root, level):
    global visited
    if root is None:
        return
    if visited[level] == False:
        print(root.data, end=" ")
        visited[level] = True
    left_view(root.left, level + 1)
    left_view(root.right, level + 1)






if __name__ == "__main__":
    t = Tree()
    root = t.create_tree()
    level = 0
    print('Left view of tree:',end=" ")
    left_view(root, level)
    print()