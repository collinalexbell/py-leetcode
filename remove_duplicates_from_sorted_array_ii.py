from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastSeen = None
        lastSeenCount = 1
        found = 0

        for i in range(len(nums)):
            if(nums[i] == lastSeen):
                lastSeenCount += 1
            else:
                lastSeen = nums[i]
                lastSeenCount = 1

            if(lastSeenCount > 2):
                found += 1
            else:
                nums[i-found] = nums[i]

        return len(nums) - found

# [1,2,3,3,3,4,5,6]