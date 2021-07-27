"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        # True when there is only one, all others are zero

        # 1 - 9
        # 1, 4, 9, 16, 25, 36, 49, 64, 81
        outcome = set()
        temp = n
        while temp != 1:
            temp2 = temp
            total = 0
            mod = 10
            while temp2 > 0:
                total += (temp2 % mod) * (temp2 % mod)
                temp2 = temp2 // mod

            if total == 1:
                return True
            elif total in outcome:
                return False
            else:
                outcome.add(total)
                temp = total

        return True
