from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        total = nums[0] 
        rv = len(nums)+1
        if(total == target):
            rv = 1

        while(end < len(nums) and start < len(nums)):
            if(total < target):
                end += 1
                if(end < len(nums)):
                    total += nums[end]
            else:
                total -= nums[start]
                start += 1

            if(total >= target):
                potential = end+1-start
                if(potential < rv):
                    rv = potential



        if(rv == len(nums)+1):
            rv = 0
        return rv


s = Solution()
print(s.minSubArrayLen(11,[1,1,1,1,1,1,1,1]))