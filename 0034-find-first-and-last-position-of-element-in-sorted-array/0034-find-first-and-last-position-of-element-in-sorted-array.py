class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l = 0
        r = len(nums)-1
        lb = len(nums)
        
        def low(nums,target):
            l = 0
            r = len(nums)-1
            lb = len(nums)
            while l <=r:
                mid = (l+(r-l)//2)
                if nums[mid] >= target:
                    lb = mid
                    r = mid-1
                else:
                    l = mid+1
            return lb
        def high(nums,target):
            l = 0
            r = len(nums)-1
            ub = len(nums)
            while l <= r:
                mid = (l+(r-l)//2)
                if nums[mid] > target:
                    ub = mid
                    r = mid-1
                else:
                    l = mid+1
            return ub

        lb = low(nums,target)
        ub = high(nums,target)

        if lb == len(nums) or nums[lb] != target:
            return [-1,-1]
        else:
            return [lb,ub-1]
        