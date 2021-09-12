from bst import BST

"""
Ceil - always rounds a number up to the next largest integer., 
eg arr = [10,12, 20,5,22]
find ceil of 14 in arr
Ans -> 20 (As 20 is greater than 14 and it is less than 22)
"""

def ceil(root, key):
    temp = root
    while temp:
        if temp.data == key:
            return temp
        elif temp.data < key:
            temp = temp.right
        else:
            res = temp
            temp = temp.left
    return res.data


if __name__ == "__main__":
    b = BST()
    root = b.create_bst()
    key = 18
    print(f'The floor of {key} is:',ceil(root, key))