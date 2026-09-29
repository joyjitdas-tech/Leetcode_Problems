class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pair = {
            ')':'(','}':'{',']':'['
        }
        if not s:
            return False
        for cd in s:
            if cd == '(' or cd == '{' or cd == '[':
                stack.append(cd)
            else:
                if not stack or stack[-1] != pair[cd]:
                    return False
                stack.pop()
        if not stack:
            return True
        else:
            return False