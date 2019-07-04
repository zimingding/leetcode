from typing import List


class Solution:
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        self.printLetter(digits, 0, '', res)
        return res

    def printLetter(self, digits: str, idx: int, curr: str, res: List[str]):
        if idx == len(digits):
            res.append(curr)
            return
        for c in self.phone[digits[idx]]:
            self.printLetter(digits, idx+1, curr + c, res)


print(Solution().letterCombinations('3'))
