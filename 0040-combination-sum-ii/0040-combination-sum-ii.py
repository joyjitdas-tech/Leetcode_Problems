class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()
        def back(index,curr,total):
            if total == target:
                result.append(curr.copy())
                return
            if total > target:
                return
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue

                total += candidates[i]
                curr.append(candidates[i])
                back(i+1,curr,total)

                curr.pop()
                total -=candidates[i]

        back(0,[],0)
        return result