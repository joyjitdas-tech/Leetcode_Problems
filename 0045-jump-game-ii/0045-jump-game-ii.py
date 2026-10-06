class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return 0

        far = 0
        count =0
        curr_end = 0
        for i in range(len(nums)-1):
            far = max(far,i+nums[i])

            if i == curr_end:
                count +=1
                curr_end = far

            if curr_end >= len(nums)-1:
                break
        return count