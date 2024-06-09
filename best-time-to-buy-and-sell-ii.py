from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        start = prices[0]
        for i in range(len(prices)):
            if((i + 1 < len(prices) and prices[i+1] < prices[i]) or i == len(prices)-1):
                max += prices[i] - start 
                if(i < len(prices)):
                    start = prices[i+1]
        return max

#[6,8,2,4]
# start = 6
# max = 0
# i = 0
# i = 1
# max = 2
# start = 2
# i = 2
# i = 3
#
