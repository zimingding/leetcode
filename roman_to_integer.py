class Solution:
    def romanToInt(self, s: str) -> int:
        r = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c == 'I':
                if i+1 < len(s) and s[i+1] == 'V':
                    r += 4
                    i += 1
                elif i+1 < len(s) and s[i+1] == 'X':
                    r += 9
                    i += 1
                else:
                    r += 1
            if c == 'V':
                r += 5
            if c == 'X':
                if i+1 < len(s) and s[i + 1] == 'L':
                    r += 40
                    i += 1
                elif i+1 < len(s) and s[i + 1] == 'C':
                    r += 90
                    i += 1
                else:
                    r += 10
            if c == 'L':
                r += 50
            if c == 'C':
                if i+1 < len(s) and s[i + 1] == 'D':
                    r += 400
                    i += 1
                elif i+1 < len(s) and s[i + 1] == 'M':
                    r += 900
                    i += 1
                else:
                    r += 100
            if c == 'D':
                r += 500
            if c == 'M':
                r += 1000

            i += 1
        return r


print(Solution().romanToInt('MCMXCIV'))
