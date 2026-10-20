class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = 0
        farq = []
        nums = []
        for i in range(len(points)):
            a = points[i][0]
            nums.append(a)
        nums.sort()
        for j in range(1, len(nums)):
            c = abs(nums[j] - nums[j - 1])
            farq.append(c)
        return max(farq)


