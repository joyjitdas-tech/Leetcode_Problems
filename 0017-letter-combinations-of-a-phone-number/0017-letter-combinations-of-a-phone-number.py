class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        Phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
    
        def back(index,curr):
            if index == len(digits):
                result.append("".join(curr))
                return
            for x in Phone[digits[index]]:
                curr.append(x)

                back(index+1,curr)

                curr.pop()
        
        back(0,[])
        return result