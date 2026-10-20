class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odds = sum(i % 2 for i in nums)
        return [0] * (len(nums) - odds) + [1] * odds