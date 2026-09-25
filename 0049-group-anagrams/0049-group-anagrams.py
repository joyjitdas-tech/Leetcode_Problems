class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        list1 = []
        hash_map = {}
        for i in range(len(strs)):
            
            s = "".join(sorted(strs[i]))
         
            hash_map.setdefault(s,[]).append(strs[i])
        for char in hash_map:
            list1.append(hash_map[char])
        return list1