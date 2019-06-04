from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                del nums[i]
            else:
                i += 1
        return len(nums)


nums = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4}
print(Solution().removeDuplicates(nums))
print(nums)
