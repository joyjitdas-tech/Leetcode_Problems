class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        result = [0]*len(nums)
        c=0
        d=1
        for i in range(0,len(nums)):
            if nums[i] > 0:
                result[c] = nums[i]
                c+=2
            else:
                result[d] = nums[i]
                d +=2
        return result