from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ['+', '-', '*', '/']
        for token in tokens:
            if token in operator:
                j = stack.pop()
                i = stack.pop()
                if token == '+':
                    stack.append(i+j)
                if token == '-':
                    stack.append(i-j)
                if token == '*':
                    stack.append(i*j)
                if token == '/':
                    stack.append(int(i/j))
            else:
                stack.append(int(token))
        return stack.pop()
