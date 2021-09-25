Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# RECURSION HERE IS A DFS APPROACH
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = [] #result
        
        if not root: # check if tree empty
            return levels
        
        
        def DFS(node,level): # breadth first search
            
            if len(levels) == level:
                levels.append([])
            
            
            # current node
            levels[level].append(node.val)
            
            if node.left: # left tree
                DFS(node.left,level+1)
            
            if node.right: # right tree
                DFS(node.right,level+1)
        
        
        DFS(root,0)
        return levels
       
       

# LEVEL BY LEVEL TRAVERSAL USING QUEUE IS A BFS APPROACH
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = [] #result
        
        if not root: # check if tree empty
            return levels
        
        queue = deque([root,])
        level = 0
        
        while queue:
            # start the level array
            levels.append([])
            
            for i in range(len(queue)):
                node = queue.popleft() # get node from start of Q 
                
                levels[level].append(node.val) # add node val in level
                
                if node.left: # left tree from pop
                    queue.append(node.left)
                if node.right: # right tree from pop
                    queue.append(node.right)
                    
            level += 1
                
        return levels
