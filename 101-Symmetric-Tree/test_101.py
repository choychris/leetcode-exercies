from solution_101 import Solution
from solution_101 import TreeNode


def tests():

    assert (
        Solution().isSymmetric(
            TreeNode(1, TreeNode(2, None, TreeNode(3, None, None)), TreeNode(2, None, TreeNode(3, None, None)))
        )
        == False
    )
