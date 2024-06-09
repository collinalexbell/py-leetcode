from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        max = 0

        for price in prices:
            if( max < price - start):
                max = price-start
            if(price < start):
                start = price
        return max


# example run
#[6,6,8,1,4]
# price = 6
# start = 6
# price = 6
# max = 0
# price = 8
# max 2
# price = 1
# start = 1
# price = 4
# max =3
