# Given the root of a binary tree, return the inorder traversal of its nodes' values.
#
#
#
# Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [1]
# Output: [1]
# Example 4:
#
#
# Input: root = [1,2]
# Output: [2,1]
# Example 5:
#
#
# Input: root = [1,null,2]
# Output: [1,2]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?


# INORDER RECURSIVE DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def traverse(node):

            if not node:
                return

            # LEFT
            if node.left:
                traverse(node.left)

            # NODE
            res.append(node.val)

            # RIGHT
            if node.right:
                traverse(node.right)

        traverse(root)
        return res


# ITERATIVE DFS (STACK)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        stack = []

        while stack or root: # even if root ends if outstanding in stack, continue
            if root:
                stack.append(root)
                root = root.left # keep pushing left trees

            else:
                temp = stack.pop() # pop last ele
                res.append(temp.val)
                root = temp.right # left right tree

        return res