"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 step

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""

# fibonacci approach
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 2

        total = 0
        first = 1
        second = 2
        for i in range(3, n + 1):
            # first: start at n = 1, jump to 3 with 2 steps
            # second: start at n = 2, jump to 3 with 1 step
            total = first + second
            first = second
            second = total

        return total
