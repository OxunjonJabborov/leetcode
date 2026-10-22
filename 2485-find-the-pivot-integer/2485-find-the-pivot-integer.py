class Solution:
    def pivotInteger(self, n: int) -> int:
        y = n * (n + 1) // 2
        x = int(sqrt(y))
        if x * x == y:
            return x
        return -1