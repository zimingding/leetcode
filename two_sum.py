from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, num in enumerate(nums):
            if target - num in cache:
                return [cache[target - num], i]
            else:
                cache[num] = i


print(Solution().twoSum([2, 7, 11, 15], 9))
