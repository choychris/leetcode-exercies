# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        def createBinaryTree(nums_list: list[int]):
            if not nums_list:
                return None

            length = len(nums_list)

            if not length:
                return None

            if length == 1:
                return TreeNode(nums_list[0], None, None)
            elif length == 2:
                return TreeNode(nums_list[0], None, TreeNode(nums_list[1], None, None))
            elif length == 3:
                return TreeNode(nums_list[1], TreeNode(nums_list[0], None, None), TreeNode(nums_list[2], None, None))
            else:
                mid = int((length - 1) / 2)
                return TreeNode(
                    nums_list[mid], createBinaryTree(nums_list[:mid]), createBinaryTree(nums_list[(mid + 1) :])
                )

        return createBinaryTree(nums)


# As pointed out by Leetcode folks, slicing is expensive. It makes the complexity to O(n log n)
# first slice is O(1 * n), second is O(2 * n/2)
class BetterSolution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        def createNode(nums_list, left_idx, right_idx):
            if left_idx > right_idx:
                return None

            mid = (left_idx + right_idx) / 2
            node = TreeNode(nums_list[mid])
            node.left = createNode(nums_list, left_idx, mid)
            node.right = createNode(nums_list, mid + 1, right_idx)

            return node

        return createNode(nums, 0, len(nums) - 1)
