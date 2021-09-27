# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:
#
# Input: root = [1]
# Output: [[1]]
# Example 3:
#
# Input: root = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS LEVEL QUEUE IMPLEMENTATION USING SWITCH
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        levels = []
        level = 0
        switch = False

        if not root:
            return levels

        queue = deque([root, ])

        while queue:
            levels.append([])

            for i in range(len(queue)):
                temp = queue.popleft()
                levels[level].append(temp.val)

                if temp.left:
                    queue.append(temp.left)

                if temp.right:
                    queue.append(temp.right)

            if switch:
                levels[level] = levels[level][::-1]
            switch = not switch

            level += 1

        return levels
