from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.searchStart(nums, target), self.searchEnd(nums, target)]

    def searchStart(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + int((hi - lo) / 2)
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                else:
                    hi = mid - 1
        return -1

    def searchEnd(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + int((hi - lo) / 2)
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                else:
                    lo = mid + 1
        return -1
