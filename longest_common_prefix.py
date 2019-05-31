from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        if not strs:
            return res
        index = 0
        next = True
        c = ''
        while next:
            for i, s in enumerate(strs):
                if index == len(s):
                    next = False
                    break
                if i == 0:
                    c = s[index]
                else:
                    if c != s[index]:
                        next = False
                        break
            if next:
                res += c
            index += 1
        return res


print(Solution().longestCommonPrefix(["flower","flow","flight"]))
