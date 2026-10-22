class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        natija = ''
        for i in range(0, k):
            natija += s[i]
        natija = natija[::-1]
        natija += s[k:]
        return natija