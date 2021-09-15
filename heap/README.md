### A Heap is a special Tree-based data structure in which the tree is a complete binary tree. Generally, Heaps can be of two types:

- Max-Heap: In a Max-Heap the key present at the root node must be greatest among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.
- Min-Heap: In a Min-Heap the key present at the root node must be minimum among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.
![heap](https://www.geeksforgeeks.org/wp-content/uploads/MinHeapAndMaxHeap.png)

### Binary Heap
A Binary Heap is a Binary Tree with following properties.
1) It’s a complete tree (All levels are completely filled except possibly the last level and the last level has all keys as left as possible). This property of Binary Heap makes them suitable to be stored in an array.

2) A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at root must be minimum among all keys present in Binary Heap. The same property must be recursively true for all nodes in Binary Tree. Max Binary Heap is similar to MinHeap.

How is Binary Heap represented?

A Binary Heap is a Complete Binary Tree. A binary heap is typically represented as an array.

The root element will be at Arr[0].
Below table shows indexes of other nodes for the ith node, i.e., Arr[i]:

- Arr[(i-1)/2]	Returns the parent node

- Arr[(2*i)+1]	Returns the left child node

- Arr[(2*i)+2]	Returns the right child node

#### The traversal method use to achieve Array representation is Level Order
![](https://www.geeksforgeeks.org/wp-content/uploads/binaryheap.png)


#### Question identification medthod for heap:-
- Heap questions mainly contains given keywords:
    - K
    - Smallest / largset
- if quaetion belogs to heap and you have been given K value then:-
    - k + smallest -> max heap
    - k + largest -> min heap