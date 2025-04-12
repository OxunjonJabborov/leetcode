class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        k = 0
        for i in range(len(nums)):
            for j in nums:
                if nums[i] > j:
                    k += 1
            ans.append(k)
            k = 0
        return ans
        
