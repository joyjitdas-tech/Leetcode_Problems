class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        for i in range(len(s)):
            map[s[i]] = map.get(s[i],0)+1
        print(map)
        
        unique = {k: v for k,v in map.items() if v == 1}

        first_unq = next(iter(unique),-1)

        if first_unq == -1:
            return -1
        else:
            return s.index(first_unq)