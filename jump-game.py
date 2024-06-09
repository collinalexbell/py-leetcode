from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        remaining = len(nums)-1
        for i in range(len(nums)):
            index = len(nums)-i-1
            if(nums[index]+index >= remaining):
                remaining = index
        if(remaining <= 0):
            return True
        else:
            return False