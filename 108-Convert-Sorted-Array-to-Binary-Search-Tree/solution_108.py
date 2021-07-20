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
