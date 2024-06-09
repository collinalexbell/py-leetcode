from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        increment = (len(nums)+1) // 2
        while(i < len(nums)):
            if(i+increment-1 < len(nums) and nums[i] == nums[i+increment-1]):
                return nums[i]
            i += 1
        assert(False)


# [3,2,3]
# [2,3,3]
# i = 0
# increment =  2
# i = 1
# if(True)
# return 3