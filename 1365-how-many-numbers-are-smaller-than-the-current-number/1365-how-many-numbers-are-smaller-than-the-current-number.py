class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        lugat = {}
        for i, num in enumerate(sorted_nums):
            if num not in lugat:
                lugat[num] = i
        javob = [lugat[num] for num in nums]
        return javob