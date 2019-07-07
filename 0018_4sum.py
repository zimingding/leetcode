from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    li = [nums[i], nums[j], nums[k], nums[l]]
                    if sum(li) == target:
                        res.append(li)
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif sum(li) > target:
                        l -= 1
                    else:
                        k += 1
        return res


print(Solution().fourSum([-1, 0, 1, 2, -1, -4], -1))
