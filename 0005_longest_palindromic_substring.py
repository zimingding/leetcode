class Solution:
    res = ''
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            self.check(s, i, i);
            self.check(s, i, i+1);
        return self.res

    def check(self, s: str, i: int, j: int):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        if j - i - 1 > len(self.res):
            self.res = s[i+1:j]


print(Solution().longestPalindrome('ab'))
