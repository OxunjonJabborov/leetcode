class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        yigindi = sum(nums)
        qoldiq = yigindi % k
        return qoldiq if qoldiq != 0 else 0