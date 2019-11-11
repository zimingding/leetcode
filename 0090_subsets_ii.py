from typing import List


class Solution:
    def __init__(self):
        self.res = []
        self.s = set()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.subsets_r(nums, 0, [])
        return self.res

    def subsets_r(self, nums: List[int], i: int, cl: List[int]):
        if i == len(nums):
            ss = ' '.join(map(str, cl))
            if ss not in self.s:
                self.s.add(ss)
                self.res.append(cl)
            return

            c1 = cl.copy()
            self.subsets_r(nums, i + 1, c1)
            c2 = c1.copy()
            c2.append(nums[i])
            self.subsets_r(nums, i + 1, c2)


res = Solution().subsetsWithDup([1,2,2])
print(res)