class Solution:
    def reverse(self, x: int) -> int:
        neg = True if x < 0 else False
        s = str(x)
        r = ''
        index = len(s)
        while index:
            index -= 1
            if s[index] == '-':
                continue
            r += s[index]
        r = int(r) * (-1 if neg else 1)
        if r > 2 ** 31 -1 or r < -2 ** 31:
            return 0
        return r


print(Solution().reverse(-123))
