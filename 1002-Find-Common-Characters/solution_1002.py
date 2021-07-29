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
