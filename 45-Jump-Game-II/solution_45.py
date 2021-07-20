# loop the possible jump, if step < previous step, update;
# step >= previous step, break;
# if land in 0, break;
# edge cose:
# .  if lenght = 1, return 0;
#   if num[0] == 0, return 0;
#   [1, 2, 3];
# https://stackoverflow.com/questions/45291759/how-can-i-get-vss-python-syntax-highlighting-in-vs-code
class Solution:
    def jump(self, nums: list[int]) -> int:
        lenght = len(nums)
        if lenght == 1 or lenght == 0:
            return 0

        if lenght == 2:
            return 1

        jump_count = 0
        currEnd = 0
        furtherest = 0

        for i in range(lenght):

            # find max jump
            if i + nums[i] > furtherest:
                furtherest = i + nums[i]

            if currEnd == i:
                jump_count += 1
                currEnd = furtherest

                if currEnd >= lenght - 1:
                    return jump_count

        return jump_count
