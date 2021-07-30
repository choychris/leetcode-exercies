"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Input: s = "leetcode"
Output: 0

Input: s = "loveleetcode"
Output: 2
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        charList = [0 for n in range(26)]

        for a in s:
            charList[ord(a) - ord("a")] += 1

        for i in range(len(s)):
            a = s[i]
            if charList[ord(a) - ord("a")] == 1:
                return i

        return -1


class SolutionTwo:
    def firstUniqChar(self, s: str) -> int:
        charDict = dict()

        for a in s:
            if a in charDict:
                charDict[a] += 1
            else:
                charDict[a] = 1

        for i in range(len(s)):
            a = s[i]
            if charDict[a] == 1:
                return i

        return -1
