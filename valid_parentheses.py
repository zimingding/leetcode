class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(', '{', '[']
        close = [')', '}', ']']
        for c in s:
            if c in open:
                stack.append(c)
            else:
                index = close.index(c)
                if not stack or open[index] != stack.pop():
                    return False
        return not stack


print(Solution().isValid('[()]'))
