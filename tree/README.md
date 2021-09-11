### 1)The maximum number of nodes at level ‘l’ of a binary tree is 2^l. 
Here level is the number of nodes on the path from the root to the node (including root and node). 

Level of the root is 0. 

This can be proved by induction. 
For root, l = 0, number of nodes = 20 = 1 
Assume that the maximum number of nodes on level ‘l’ is 2l 

Since in Binary tree every node has at most 2 children, next level would have twice nodes, i.e. 2 * 2l 

### 2)The Maximum number of nodes in a binary tree of height ‘h’ is 2^(h+1) – 1. 
Here the height of a tree is the maximum number of nodes on the root to leaf path. Height of a tree with a single node is considered as 1. 

This result can be derived from point 2 above. A tree has maximum nodes if all levels have maximum nodes.
 So maximum number of nodes in a binary tree of height h is 1 + 2 + 4 + .. + 2h. This is a simple geometric series with h terms and sum of this series is 2^(h– 1). 

In some books, the height of the root is considered as 0. In this convention, the above formula becomes 2^(h+1) – 1 

### 3) In a Binary Tree with N nodes, minimum possible height or the minimum number of levels is? Log2(N+1) ?   
This can be directly derived from point 2 above. If we consider the convention where the height of a root node is considered as 0, then above formula for minimum possible height becomes | Log2(N+1) | – 1 