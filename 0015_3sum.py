from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                list = [nums[i], nums[j], nums[k]]
                total = sum(list)
                if total == 0:
                    res.append(list)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
        return res


print(Solution().threeSum([-1,0,1,2,-1,-4]))
