from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0 and i < len(arr) - 1:
                i += 1
                self.shift1(arr, i)
                arr[i] = 0
            i += 1

    def shift1(self, arr: List[int], i: int) -> None:
        n = len(arr) - 1
        while n > i:
            arr[n] = arr[n-1]
            n -= 1


arr = [1, 0, 2, 3, 0, 4, 5, 0]
Solution().duplicateZeros(arr)
print(arr)
