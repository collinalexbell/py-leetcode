from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        tmp = nums[-k:]
        for i in range(len(nums)-k):
            nums[-i-1] = nums[-k-1-i]
        for i in range(k):
            nums[i] = tmp[i]

## example to think through
# [1,2,3,4]
# k = 2
# [3,4]
# [1,2,1,2]
# [3,4,1,2]

## run example
# tmp = [3, 4]
# i = 0 in range(2)
# nums[2] = nums[0]
# [1,2,1,4]
# i = 1 in range(2)
# nums[3] = nums[1]
# [1,2,1,2]
# i = 0 in range(2)
# nums[0] = tmp[0]
# [3,2,1,2]
# i = 0 in range(2)
# nums[1] = tmp[1]
# [3,4,1,2]