from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1
        while i > len(nums) * -1:
            if nums[i] > nums[i - 1]:
                break
            i -= 1
        if i == len(nums) * -1:
            nums.reverse()
            return
        idx = i
        j = i
        val = nums[i]
        while j < 0:
            if nums[i - 1] < nums[j] < val:
                val = nums[j]
                idx = j
            j += 1
        nums[i - 1], nums[idx] = nums[idx], nums[i-1]

        end = nums[i:]
        end.sort()
        nums[i:] = end


nums = [2, 3, 1]
Solution().nextPermutation(nums)
print(nums)
