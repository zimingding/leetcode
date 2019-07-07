class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = max(len(num1), len(num2))
        res = ''
        while len(num1) < n:
            num1 = '0' + num1
        while len(num2) < n:
            num2 = '0' + num2
        idx = -1
        bit = 0
        while idx >= -1 * n:
            sum = int(num1[idx]) + int(num2[idx]) + bit
            res = str(sum % 10) + res
            bit = int(sum / 10)
            idx -= 1
        if bit:
            res = '1' + res
        return res


print(Solution().addStrings('123', '89'))
