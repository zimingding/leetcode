class Solution:
    def myAtoi(self, str: str) -> int:
        words = str.strip().split()
        if not words:
            return 0
        try:
            res = int(self.clean(words[0]))
        except ValueError:
            return 0

        INT_MAX = pow(2, 31) - 1
        INT_MIN = -1 * pow(2, 31)

        if res > INT_MAX:
            res = INT_MAX

        if res < INT_MIN:
            res = INT_MIN

        return res

    def clean(self, str: str) -> str:
        ret = ''
        for i, c in enumerate(str):
            if c.isdigit():
                ret += c
            elif i == 0 and c == '+':
                ret += c
            elif i == 0 and c == '-':
                ret += c
            else:
                break
        return ret


print(Solution().myAtoi('42'))
