class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def back(start,current):
            if len(nums) == len(current):
                result.append(current.copy())
                return
            for num in nums:
                if num in current:
                    continue
                
                current.append(num)
                back(start+1,current)
                current.pop()

        back(0,[])

        return result