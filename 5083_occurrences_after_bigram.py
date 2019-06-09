from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        words = text.split();
        for i, v in enumerate(words):
            if v == first and i < len(words) - 2 and words[i+1] == second:
                res.append(words[i+2])
        return res


print(Solution().findOcurrences('we will we will rock you', 'we', 'will'))