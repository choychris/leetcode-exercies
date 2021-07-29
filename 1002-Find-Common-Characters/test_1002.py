from solution_1002 import Solution


def test():
    assert Solution().commonChars(["cool", "lock", "cook"]) == ["c", "o"]

    assert Solution().commonChars(["bella", "label", "roller"]) == ["e", "l", "l"]
