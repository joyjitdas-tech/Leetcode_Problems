class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        ans = []
        sum = 0
        min_win = len(nums)+1
        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                min_win = min(min_win,right-left+1)
                
                sum -= nums[left]
                left += 1
            
        if min_win == len(nums) +1:
            return 0
        return min_win