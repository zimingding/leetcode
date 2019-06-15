class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle:
            return 0

        for i in range(len(haystack)):
            if i + len(needle) - 1 < len(haystack) and haystack[i:i+len(needle)] == needle:
                return i
        return -1


print(Solution().strStr('hello', 'll'))
