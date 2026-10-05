class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def low():
            left = 0
            right = len(nums) -1
            lb = len(nums)
            
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] >= target:
                    lb = mid
                    right = mid -1
                else:
                    left = mid+1
            return lb
        def high():
            left = 0
            right = len(nums) -1
            ub = len(nums)
            
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] > target:
                    ub = mid
                    right = mid -1
                else:
                    left = mid+1
            return ub
        lb = low()
        ub = high()
        if lb == len(nums) or nums[lb] != target:
            return [-1,-1]
        else:
            return [lb,ub-1]