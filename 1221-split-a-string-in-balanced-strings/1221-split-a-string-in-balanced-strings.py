class Solution:
    def balancedStringSplit(self, s: str) -> int:
        k = 0
        r = 0
        l = 0
        for i in s:
            if i == 'R':
                r += 1
            elif i == 'L':
                l += 1
            if l == r:
                k += 1
                r = 0 
                l = 0
        return k