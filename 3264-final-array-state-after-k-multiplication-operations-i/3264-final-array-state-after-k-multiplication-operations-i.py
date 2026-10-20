class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        i = 1
        while i <= k:
            a = min(nums)
            if a in nums:
                o = nums.index(a)
                nums[o] = a * multiplier
            i += 1
        return nums

            

