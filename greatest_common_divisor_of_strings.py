class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        n = 1
        while n <= len(str2):
            t = str2[:n]
            if self.canDivide(str1, t) and self.canDivide(str2, t):
                res = t
            n += 1
        return res

    def canDivide(self, s: str, t: str) -> bool:
        if len(s) % len(t) != 0:
            return False
        n = len(s) / len(t)
        r = ""
        while n > 0:
            r += t
            n -= 1
        return r == s


print(Solution().gcdOfStrings("FBFKOXFBFKOXFBFKOXFBFKOXFBFKOX", "FBFKOXFBFKOXFBFKOXFBFKOXFBFKOXFBFKOXFBFKOXFBFKOXFBFKOX"))
