class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        natija = []
        while columnNumber > 0:
            columnNumber -= 1
            qoldiq = columnNumber % 26
            natija.append(chr(ord("A") + qoldiq))
            columnNumber //= 26
        return "".join(reversed(natija))
