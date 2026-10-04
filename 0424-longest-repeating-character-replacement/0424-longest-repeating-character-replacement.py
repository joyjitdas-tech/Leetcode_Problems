class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_c = 0
        ans= 0
        c = {}
        for right in range(len(s)):
            c[s[right]] = c.get(s[right],0)+1
            max_c = max(max_c,c[s[right]])

            while (right-left+1) - max_c > k:
                c[s[left]] -=1
                left +=1

            ans = max(ans,right-left+1)

        return ans       
