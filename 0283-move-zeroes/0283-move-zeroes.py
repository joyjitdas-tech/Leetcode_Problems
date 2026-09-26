class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp = []
        for num in nums:
            if num != 0 :
                temp.append(num)
        print(temp)
        k = len(temp)
        for i in range(0,n):
            if i < k:
                nums[i] = temp[i]
            else:
                nums[i] = 0

        