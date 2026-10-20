class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        nat = 0
        natija = 0
        for i in reversed(s):
            e = d[i]
            if e < nat:
                natija -= e
            else:
                natija += e
            nat = e
        return natija