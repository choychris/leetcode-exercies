from solution_91 import Solution


def tests():
    assert Solution().numDecodings("12") == 2
    assert Solution().numDecodings("226") == 3
    assert Solution().numDecodings("") == 0
    assert Solution().numDecodings("220") == 1
    assert Solution().numDecodings("260") == 0
    assert Solution().numDecodings("27") == 1
    assert Solution().numDecodings("2301") == 0
    assert Solution().numDecodings("2311") == 4
