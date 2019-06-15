class Solution:
    def countAndSay(self, n: int) -> str:
        s = ''
        i = 0
        while i < n:
            s = self.say(s)
            i += 1
        return s

    def say(self, s: str) -> str:
        if not s:
            return '1'
        r = ''
        i = 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            r += str(j-i) + str(s[i])
            i = j
        return r


print(Solution().countAndSay(5))
