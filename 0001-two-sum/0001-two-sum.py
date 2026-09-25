class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i in range(len(nums)):
            num = nums[i]
            temp = target - num
            if temp in hash_map:
                return [hash_map[temp],i]
            hash_map[num] = i
        return []