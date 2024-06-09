from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m):
            nums1[n+i] = nums1[i]

        mi, ni = 0, 0

        for i in range(m+n):
            val = None

            if(mi<m and ni<n):
                if(nums1[mi+n] < nums2[ni]):
                    val = nums1[mi+n]
                    mi+=1
                else:
                    val = nums2[ni]
                    ni+=1
            elif(ni == n):
                val = nums1[mi+n]
                mi+=1
            else:
                val = nums2[ni]
                ni+=1
            
            nums1[i] = val