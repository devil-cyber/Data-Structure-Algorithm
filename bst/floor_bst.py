from bst import BST

"""
Floor - means greatest integer less than or equal to x, 
eg arr = [10,12, 20,5,22]
find floor of 14 in arr
Ans -> 12 (As 12 less than 14 and it is greater than 10)
"""

def floor(root, key):
    temp = root
    while temp:
        if temp.data == key:
            return temp
        elif temp.data > key:
            temp = temp.left
        else:
            res = temp
            temp = temp.right
    return res.data


if __name__ == "__main__":
    b = BST()
    root = b.create_bst()
    key = 13
    print(f'The floor of {key} is:',floor(root, key))