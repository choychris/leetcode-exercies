# find all the rectangles(group of boxes), where 1<=hc<=h, 1<=vc<=w
# intersect points of the cuts, +original points with 0 e.g (0, 0), (1, 0)
# 4 points => 1 group
# max area = max hc, vc => furtherest 2 points of hc, and vc
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list[int], verticalCuts: list[int]) -> int:
        def merge(left: list[int], right: list[int]):
            l = 0
            r = 0
            sort = []
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    sort.append(left[l])
                    l += 1
                else:
                    sort.append(right[r])
                    r += 1

            while l < len(left):
                sort.append(left[l])
                l += 1

            while r < len(right):
                sort.append(right[r])
                r += 1

            return sort

        def sort(to_sort: list[int], l, r):
            if r > l:
                mid = l + (r - l) // 2
                left = sort(to_sort, l, mid)
                right = sort(to_sort, mid + 1, r)
                merged = merge(left, right)

                return merged
            else:
                return [to_sort[l]]

        diff_h = 0

        if len(horizontalCuts) == 1:
            diff_h = max(h - horizontalCuts[0], horizontalCuts[0])
        else:
            sortedHorizontalCuts = sort(horizontalCuts, 0, len(horizontalCuts) - 1)
            sortedHorizontalCuts = [0] + sortedHorizontalCuts + [h]
            for i in range(len(sortedHorizontalCuts) - 1):
                diff_h = max(diff_h, sortedHorizontalCuts[i + 1] - sortedHorizontalCuts[i])

        diff_w = 0

        if len(verticalCuts) == 1:
            diff_w = max(w - verticalCuts[0], verticalCuts[0])
        else:
            sortedVerticalCuts = sort(verticalCuts, 0, len(verticalCuts) - 1)
            sortedVerticalCuts = [0] + sortedVerticalCuts + [w]
            for i in range(len(sortedVerticalCuts) - 1):
                diff_w = max(diff_w, sortedVerticalCuts[i + 1] - sortedVerticalCuts[i])

        largest = (diff_h * diff_w) % (pow(10, 9) + 7)
        return largest
