class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        farq = 0
        for i in range(len(s)):
            farq += abs(s.index(s[i]) - t.index(s[i]))
        return farq
                