class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums.count(i) > 1:
                ans.append(i)
                i += 1
        return ans