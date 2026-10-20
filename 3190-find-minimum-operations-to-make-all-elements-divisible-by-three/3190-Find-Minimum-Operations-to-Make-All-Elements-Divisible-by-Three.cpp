class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        k = 0
        for i in nums:
            qoldiq = i % 3 
            if qoldiq == 1:
                k += 1
            elif qoldiq == 2:
                k += 1
        return k