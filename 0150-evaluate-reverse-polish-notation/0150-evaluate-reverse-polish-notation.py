class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        op = ['+','-','*','/']
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in op:
                stack.append(int(tokens[i]))
            else:
                print(tokens[i])
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == '+':
                    stack.append(b+a)
                if tokens[i] == '-':
                    stack.append(b-a)
                if tokens[i] == '*':
                    stack.append(b * a)
                if tokens[i] == '/':
                    stack.append(int(b / a))
        return stack[-1]