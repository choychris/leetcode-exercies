class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        start = words[0]
        common = []
        for c in start:
            count = 0
            for i in range(1, len(words)):
                w = words[i]
                if c in w:
                    count += 1
                    words[i] = w.replace(c, "", 1)
                else:
                    break

            if count == len(words) - 1:
                common.append(c)

        return common


class SolutionTwo:
    def commonChars(self, words: list[str]) -> list[str]:
        count = [float("inf")] * 26
        common = []

        for w in words:
            inner_count = [0] * 26
            for c in w:
                inner_count[ord(c) - ord("a")] += 1

            for i in range(26):
                if inner_count[i] < count[i]:
                    count[i] = inner_count[i]

        for i in range(26):
            cnt = count[i]
            for j in range(cnt):
                common.append(chr(97 + i))

        return common
