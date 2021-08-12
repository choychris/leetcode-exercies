# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
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


class BFSSolution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth = 0
        queue = [root]
        while len(queue):
            depth += 1
            newQueue = []
            for v in queue:
                if v.left:
                    newQueue.append(v.left)
                if v.right:
                    newQueue.append(v.right)
            queue = newQueue

        return depth


class DFSSolution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth = 0

        stack = [root]

        while stack:
            v = stack[-1]
            if v.left:
                l = v.left
                v.left = None
                stack[-1] = v
                stack.append(l)
            elif v.right:
                r = v.right
                v.right = None
                stack[-1] = v
                stack.append(r)
            else:
                depth = max(depth, len(stack))
                stack.pop()

        return depth
