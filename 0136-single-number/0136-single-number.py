class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        natija = 0
        for i in nums:
            natija ^= i
        return natija