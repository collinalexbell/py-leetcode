from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        hindex = len(citations)
        count = 0
        for citationNum in citations:
            while(count < hindex and hindex > citationNum):
                    hindex -= 1
            if(citationNum >= hindex):
                count += 1
            if(count >= hindex):
                 return hindex
                