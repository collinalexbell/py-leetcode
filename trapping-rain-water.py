from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        highestSeenLeft = []        
        highestSeenRight = []
        for h in height:
            if(len(highestSeenLeft) > 0 and highestSeenLeft[-1] > h):
                highestSeenLeft.append(highestSeenLeft[-1])
            else:
                highestSeenLeft.append(h)

        for h in reversed(height):
            if(len(highestSeenRight) > 0 and highestSeenRight[-1] > h):
                highestSeenRight.append(highestSeenRight[-1])
            else:
                highestSeenRight.append(h)
        highestSeenRight.reverse()
        
        rv = 0 
        for i in range(len(height)):
            rv += max(0,min(highestSeenLeft[i], highestSeenRight[i]) - height[i])
        return rv

