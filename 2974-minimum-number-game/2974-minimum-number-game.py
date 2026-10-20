class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        alice = 0
        bob = 0
        arr = []
        nums.sort()
        # m = min(nums)
        for i in range(0, len(nums), 2):
            alice = nums[i]
            bob = nums[i + 1]
            arr.append(bob)
            arr.append(alice)
        return arr