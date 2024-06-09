class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        maxVal = 0

        while (start < end):
            total = min(height[start], height[end]) * (end-start)
            if(total > maxVal):
                maxVal = total
            if(height[start] > height[end]):
                end -= 1
            else:
                start += 1
        return maxVal