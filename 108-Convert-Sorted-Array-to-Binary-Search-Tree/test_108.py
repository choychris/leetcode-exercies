from solution_108 import Solution
from solution_108 import TreeNode


class Matcher:
    expected: TreeNode

    def __init__(self, expected: TreeNode):
        self.expected = expected

    def __eq__(self):
        print("TODO __eq__")
        # TODO: write for test


def tests():
    Solution().sortedArrayToBST([-10, -3, 0, 5, 9]) == TreeNode(0, TreeNode(-3, None, None), TreeNode(5, None, None))
