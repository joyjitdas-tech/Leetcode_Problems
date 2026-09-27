class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        temp = ""
        #48-57 for 0-9
        for ch in s:
            x = ord(ch)
            if (x>=48 and x<=57) or (x>=97 and x<=122):
                temp += ch
        l = 0
        r = len(temp)-1
        while l < r:
            if temp[l] == temp[r]:
                l+=1
                r-=1
            else:
                return False
        return True
        