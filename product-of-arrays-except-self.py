from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        upToAPoint = []
        downToAPoint = []
        for num in nums:
            if(len(upToAPoint) == 0):
                upToAPoint.append(num)
            else:
                upToAPoint.append(num*upToAPoint[len(upToAPoint)-1])
        for num in reversed(nums):
            if(len(downToAPoint) == 0):
                downToAPoint.append(num)
            else:
                downToAPoint.append(num*downToAPoint[len(downToAPoint)-1])

        rv = []
        downToAPoint.reverse()
        for i in range(len(nums)):
            a = 1
            b = 1
            if(i != 0):
                a = upToAPoint[i-1]
            if(i != len(nums)-1):
                b = downToAPoint[i+1]
            rv.append(a*b)            
        return rv



#[1,2,3,4]
#[1,2,6,24]
#[4,12,24,24]