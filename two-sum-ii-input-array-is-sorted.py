from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1

        while(True):
            total = numbers[start] + numbers[end]
            if(total > target):
                end -= 1
            elif(total < target):
                start += 1
            else:
                return [start+1, end+1]

s = Solution()
print(s.twoSum([0,0,1,2,4], 3))
