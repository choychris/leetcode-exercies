class Solution:
    def myAtoi(self, s: str) -> int:
        print("todo")

        total = 0
        state = 0
        sign = 1

        for n in s:
            if n == " ":
                if state == 0:
                    continue
                else:
                    break
            if 48 <= ord(n) and ord(n) <= 57:  # number
                state = 2
                total = total * 10 + (ord(n) - ord("0"))
                continue
            elif n == "+" or n == "-":
                if state == 0:
                    state = 1
                    if n == "-":
                        sign = -1
                else:
                    break
            else:
                break

        if sign < 0:
            return max(-total, -(2 ** 31))
        else:
            return min(total, 2 ** 31 - 1)
