class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        map = {}
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))

            map.setdefault(s,[]).append(strs[i])

        return list(map.values())