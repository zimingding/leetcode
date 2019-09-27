from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            dict[i] = True
        res = 1
        while res in dict.keys():
            res += 1
        return res
