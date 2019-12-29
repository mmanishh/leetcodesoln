import statistics
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)<1 and len(nums2)>=1:
            return statistics.median(nums2)
        elif len(nums2)<1 and len(nums1)>=1:
            return statistics.median(nums1)
        else:
            first = sum(nums1)/len(nums1)
            second = sum(nums2)/len(nums2)
            return (first+second)/2

if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1,3,5,6,7],[2,4]))