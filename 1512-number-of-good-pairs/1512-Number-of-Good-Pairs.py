class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        for i in range(len(nums)):
            for j in nums[i+1:]:
                if nums[i] == j:
                    good_pairs += 1
        return good_pairs