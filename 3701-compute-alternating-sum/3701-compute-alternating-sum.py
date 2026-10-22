class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        juft = 0
        toq = 0
        for i in range(0, len(nums), 2):
            juft += nums[i]
        for i in range(1, len(nums), 2):
            toq += nums[i]
        return juft - toq