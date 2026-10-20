class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0]
        rightSum = [0]
        n = len(nums)
        a = 0
        ans = []
        for i in range(n - 1):
            a = leftSum[i] + nums[i]
            leftSum.append(a)
        for i in range(n - 1):
            a = rightSum[i] + nums[n-i-1]
            rightSum.append(a)
        rightSum.reverse()
        for i in range(len(nums)):
            ans.append(abs(leftSum[i] - rightSum[i]))
        # print(len(leftSum), len(rightSum), len(nums))
        return ans