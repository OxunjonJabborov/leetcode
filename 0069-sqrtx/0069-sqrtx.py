class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        taxmin = x / 2
        while True:
            yangi = (taxmin + x / taxmin) / 2
            if abs(yangi - taxmin) <= 0.001:
                return int(yangi)
            taxmin = yangi