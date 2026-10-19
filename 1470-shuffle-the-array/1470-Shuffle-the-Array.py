class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * (2 * n)
        ans[::2] = nums[:n]
        ans[1::2] = nums[n:]
        return ans