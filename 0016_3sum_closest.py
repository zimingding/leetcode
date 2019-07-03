import sys
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        gap = sys.maxsize
        res = 0
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = sum([nums[i], nums[j], nums[k]])
                if total == target:
                    return total
                elif total > target:
                    if total - target < gap:
                        gap = total - target
                        res = total
                    k -= 1
                else:
                    if target - total < gap:
                        gap = target - total
                        res = total
                    j += 1
        return res


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
