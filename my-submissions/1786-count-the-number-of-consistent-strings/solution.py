class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        k = 0
        for i in words:
            for j in i:
                a = True
                if j not in allowed:
                    a = False
                    break
            if a:
                k += 1
        return k


