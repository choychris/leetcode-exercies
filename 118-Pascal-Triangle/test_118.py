from solution_118 import Solution


def tests():

    assert Solution().generate(int(5)) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
    ]

    assert Solution().generate(int(1)) == [[1]]
