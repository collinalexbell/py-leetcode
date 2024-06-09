from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        lastSeen = None
        found = 0
        for i in range(len(nums)):
            if(lastSeen == nums[i]):
                found += 1
            else:
                nums[i-found] = nums[i]
            lastSeen = nums[i]
        return len(nums) - found
        


# [1,2,2,3,4,4,5]

# lastSeen = None
# i = 0 nothing happens; nums[i] = nums[i-found]
# i = 1 nothing happens
# i = 2 found += 1
# i = 3 nums[3] = nums[2]

# len(nums) - found