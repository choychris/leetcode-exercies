from solution_17 import Solution
import unittest
def tests():
  actual = Solution().letterCombinations("23")
  expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
  unittest.TestCase().assertCountEqual(actual, expected)