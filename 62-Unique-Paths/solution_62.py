class DPSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0

        if m == 1 or n == 1:
            return 1

        dp: list = [None] * n
        for i in range(n):
            dp[i] = 1

        for i in range(m):
            for j in range(n):
                dp[j] += dp[j - 1]

        return dp[n - 1]
