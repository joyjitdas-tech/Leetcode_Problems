class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in hash_map:
                hash_map[s[i]] +=1
            else:
                hash_map[s[i]] = 1
        for j in range(len(t)):
            if t[j] not in hash_map:
                return False
            hash_map[t[j]] -=1
        for char in hash_map:
            if hash_map[char] != 0:
                return False
        return True
