from solution_104 import Solution
from solution_104 import BFSSolution
from solution_104 import DFSSolution
from solution_104 import TreeNode


def tests():
    assert Solution().maxDepth(TreeNode(1, None, TreeNode(2, None, None)))

    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert Solution().maxDepth(root) == 3
    assert BFSSolution().maxDepth(root) == 3
    assert DFSSolution().maxDepth(root) == 3
