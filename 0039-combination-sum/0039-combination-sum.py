class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def back(start,current,total):
            if total == target:
                result.append(current.copy())
                return
            if total > target:
                return 
            for i in range(start,len(candidates)):
                current.append(candidates[i])
                total += candidates[i]
                back(i,current,total)

                current.pop()
                total -= candidates[i]
        back(0,[],0)
        return result