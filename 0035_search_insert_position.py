from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, v in enumerate(nums):
            if v == target:
                return i

        for i, v in enumerate(nums):
            if v > target:
                return i

        return len(nums)
