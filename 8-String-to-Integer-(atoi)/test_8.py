from solution_8 import Solution


def tests():

    assert Solution().myAtoi("42") == 42

    assert Solution().myAtoi("+42") == 42

    assert Solution().myAtoi("-42") == -42

    assert Solution().myAtoi("+-42") == 0

    assert Solution().myAtoi("++42") == 0

    assert Solution().myAtoi("   -42") == -42

    assert Solution().myAtoi("4193 with words") == 4193

    assert Solution().myAtoi("words and 987") == 0

    assert Solution().myAtoi("-91283472332") == -2147483648
