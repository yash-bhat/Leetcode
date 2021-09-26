class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

print(tree.val,tree.left.val,tree.right.val)