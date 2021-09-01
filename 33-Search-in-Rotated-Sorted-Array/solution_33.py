class Solution:
    def search(self, nums: list[int], target: int) -> int:
      if len(nums) == 1:
        if nums[0] == target:
          return 0
        else:
          return -1
      
      def divide(ans, start, end):
        if ans != -1:
          return ans

        if start >= end:
          if nums[end] == target:
            return end
          return -1

        mid = (end - start)//2 + start
        first = divide(ans, start, mid)

        if first != -1:
          return first
        else:
          second = divide(ans, mid+1, end)
          return second

      res = divide(-1, 0, len(nums) - 1)

      return res

class BinarySearchSolution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        def bSearch(start, end):
            if start >= end:
                if nums[end] == target:
                    return end
                else:
                    return -1

            mid = (end - start) // 2 + start
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return bSearch(start, mid)
            elif nums[mid] < target:
                return bSearch(mid + 1, end)
            else:
                return -1

        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return bSearch(mid+1, len(nums)-1)
        elif nums[mid] < target:
            return bSearch(0, mid)
        else:
            return -1
        
