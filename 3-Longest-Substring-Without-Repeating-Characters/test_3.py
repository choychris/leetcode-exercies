from solution_3 import Solution


def tests():
    assert Solution().lengthOfLongestSubstring("au") == 2

    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3

    assert Solution().lengthOfLongestSubstring("bbbbb") == 1

    assert Solution().lengthOfLongestSubstring("pwwkew") == 3

    assert Solution().lengthOfLongestSubstring("") == 0
