from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        found = 0
        for i in range(len(nums)):
            if(nums[i] == val):
                found += 1
            else:
                nums[i-found] = nums[i]
        return len(nums) - found

#[1,2,3,4,5]
# i = 0
# v = 1

#i = 1
#v = 2
#found = 1

#i = 2
#v = 3
#nums[i-found] = v

