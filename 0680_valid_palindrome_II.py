class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.isPalindrome(s, i + 1, j) or self.isPalindrome(s, i, j - 1)
            i += 1
            j -= 1
        return True

    def isPalindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


print(Solution().validPalindrome('abca'))
