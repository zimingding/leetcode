from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.recurse('', n, 0, 0, res)
        return res

    def recurse(self, curr: str, n: int, i: int, j: int, result: List):
        if len(curr) == 2 * n:
            result.append(curr)
        if i < n:
            self.recurse(curr + '(', n, i + 1, j, result)
        if j < n and j < i:
            self.recurse(curr + ')', n, i, j + 1, result)


print(Solution().generateParenthesis(9))
