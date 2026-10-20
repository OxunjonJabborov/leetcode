class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        t = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                a = nums2[j] * k
                if nums1[i] % a == 0:
                    t += 1
        return t