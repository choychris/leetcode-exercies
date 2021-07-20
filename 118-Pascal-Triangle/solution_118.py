# numRows >= 1,
# simple case if numRows = 1, return [[1]]
# what if null ? return null
# start and end alawys 1
# prev[1] + prev[2] => next[1]
# prev[2] + prev[3] => next[2]


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if not numRows:
            return None
        if numRows == 1:
            return [[1]]

        pascal_triangle = [[1], [1, 1]]

        while len(pascal_triangle) < numRows:
            next_len = len(pascal_triangle) + 1
            mid = int((next_len - 1) / 2)
            row = [1]
            n = 0
            while n < mid:
                last = pascal_triangle[-1]
                row.append(last[n] + last[n + 1])
                n += 1

            if next_len % 2 != 0:
                row += row[::-1][1:]
            else:
                row += row[::-1]

            pascal_triangle.append(row)

        return pascal_triangle
