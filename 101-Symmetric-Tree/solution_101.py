# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursion
# check from last - left, last - right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return root
        if not root.left and not root.right:
            return True

        def checkMirror(leftNode, rightNode):
            if not leftNode and not rightNode:
                return True
            if (not rightNode) and leftNode:
                return False
            if (not leftNode) and rightNode:
                return False

            if leftNode.val == rightNode.val:
                l = checkMirror(leftNode.right, rightNode.left)
                r = checkMirror(leftNode.left, rightNode.right)
                return l and r
            else:
                return False

        sol = checkMirror(root.left, root.right)
        return sol
