class Solution:
    def fib(self, n: int) -> int:
        dp = [-1]*(n+1)

        def helper(n,dp):
            if n<=1:
                return n
            if dp[n] != -1:
                return dp
            dp = helper(n-1,dp)+helper(n-2,dp)

            return dp
        return helper(n,dp)