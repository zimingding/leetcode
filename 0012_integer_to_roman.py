class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''

        for i, v in enumerate(str(num)[::-1]):
            if i == 0:
                v = int(v)
                if v == 9:
                    res = 'IX'
                elif v > 4:
                    res = 'V' + 'I' * (v - 5)
                elif v == 4:
                    res = 'IV'
                else:
                    res = 'I' * v
            elif i == 1:
                v = int(v)
                if v == 9:
                    res = 'XC' + res
                elif v > 4:
                    res = 'L' + 'X' * (v - 5) + res
                elif v == 4:
                    res = 'XL' + res
                else:
                    res = 'X' * v + res
            elif i == 2:
                v = int(v)
                if v == 9:
                    res = 'CM' + res
                elif v > 4:
                    res = 'D' + 'C' * (v - 5) + res
                elif v == 4:
                    res = 'CD' + res
                else:
                    res = 'C' * v + res
            else:
                v = int(v)
                res = 'M' * v + res

        return res


print(Solution().intToRoman(401))
