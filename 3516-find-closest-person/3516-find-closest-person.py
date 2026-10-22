class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        farq1 = abs(z - x)
        farq2 = abs(y - z)
        if farq1 < farq2:
            return 1
        elif farq1 > farq2:
            return 2
        else: 
            return 0