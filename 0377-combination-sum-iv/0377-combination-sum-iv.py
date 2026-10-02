class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        result = []
        count = 0
        dp = [-1]*(target+1)
        def back(remaining):
            if remaining == 0:
                
                return 1
            if remaining < 0:
                return 0
            total = 0
            if dp[remaining] != -1:
                return dp[remaining]

            for i in range(len(nums)):
                
                total += back(remaining-nums[i])

                
            dp[remaining] = total
            return total
        return back(target)

       