class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        map = {0: 1}

        for i in range(len(nums)):
            prefix += nums[i]

            need = prefix - k

            if need in map:
                count += map[need]

            map[prefix] = map.get(prefix, 0) + 1

        return count