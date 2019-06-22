class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ''
        i = 0
        sub = []
        loop = 1 + numRows - 2
        if loop == 0:
            return s
        j = 0
        while i < len(s):
            index = j % loop
            if index == 0:
                t = s[i:i + numRows]
                i += numRows
                while len(t) < numRows:
                    t += ' '
                sub.append(list(t))
            else:
                a = list(' '*numRows)
                a[numRows-index-1] = s[i]
                i += 1
                sub.append(a)
            j += 1

        for n in range(numRows):
            for m in range(len(sub)):
                res += sub[m][n].strip()

        return res


print(Solution().convert('P', 2))
