class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)
        soni = 0
        for w in words:
            if set(w).issubset(s):
                soni += 1
        return soni

