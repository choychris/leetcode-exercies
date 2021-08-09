# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: list[TreeNode]) -> int:
        if not root:
          return 0
        if not root.right and not root.left:
          return 1
        
        def getBranchDepth(node):
            if not node:
              return 0

            depth = 1
            leftDepth = getBranchDepth(node.left)
            rightDepth = getBranchDepth(node.right)

            return depth + max(leftDepth, rightDepth)
          
        return getBranchDepth(root)
