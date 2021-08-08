class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "" or s[0] == "0":
            return 0

        dp: list = [0] * len(s)
        dp[0] = 1
        dp[1] = 0 if ord(s[1]) == 0 else 1
        preDigit = ord(s[0]) - ord("0")
        for i in range(1, len(s)):
            digit = ord(s[i]) - ord("0")
            if digit == 0 and preDigit * 10 + digit > 26:
                return 0
            elif digit == 0:
                dp[i] = dp[i - 2] if i > 1 else dp[i - 1]
            elif preDigit * 10 + digit > 26:
                dp[i] = dp[i - 1]
            elif i == 1:
                dp[i] += dp[i - 1]
            else:
                dp[i] = dp[i - 1] + dp[i - 2]

            preDigit = digit

        return dp[-1]
