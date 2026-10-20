class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n = 0
        for i in nums1:
            n += 1
        
        n //= 2
        median = 0.0
        if len(nums1) % 2 == 0:
            median += (nums1[n] + nums1[n - 1]) / 2
        else:
            median += nums1[n]
        return median 