from solution_387 import Solution
from solution_387 import SolutionTwo


def tests():
    assert Solution().firstUniqChar("leetcode") == 0

    assert Solution().firstUniqChar("loveleetcode") == 2

    assert Solution().firstUniqChar("aabb") == -1

    assert SolutionTwo().firstUniqChar("leetcode") == 0

    assert SolutionTwo().firstUniqChar("loveleetcode") == 2

    assert SolutionTwo().firstUniqChar("aabb") == -1
