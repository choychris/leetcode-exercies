from solution_1002 import Solution
from solution_1002 import SolutionTwo


def test():
    assert Solution().commonChars(["cool", "lock", "cook"]) == ["c", "o"]

    assert Solution().commonChars(["bella", "label", "roller"]) == ["e", "l", "l"]

    assert SolutionTwo().commonChars(["cool", "lock", "cook"]) == ["c", "o"]

    assert SolutionTwo().commonChars(["bella", "label", "roller"]) == ["e", "l", "l"]
