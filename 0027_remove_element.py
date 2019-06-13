from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j, v in enumerate(nums):
            if v != val:
                nums[i] = v
                i += 1
        return i


nums = []
print(Solution().removeElement(nums, 2))
print(nums)
