class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        k = 0
        for i in nums:
            k += i
            ans.append(k)
        return ans