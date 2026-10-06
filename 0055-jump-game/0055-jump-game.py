class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_r = 0

        for i in range(len(nums)):
            if i > max_r:
                return False
            max_r=max(max_r,nums[i]+i)

            if max_r == len(nums)-1:
                return True
        return True