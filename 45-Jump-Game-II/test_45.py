from solution_45 import Solution


def tests():
    assert Solution().jump([1, 2, 1]) == 2
    assert Solution().jump([3, 2, 1]) == 1
    assert Solution().jump([2, 3, 1, 1, 4]) == 2
    assert Solution().jump([2, 3, 0, 1, 4]) == 2
    assert Solution().jump([1, 1, 1, 1, 1]) == 4
    assert Solution().jump([7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]) == 2
