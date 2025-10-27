class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        bolinadi = []
        bolinmaydi = []
        for i in range(1, n + 1):
            if i % m == 0:
                bolinadi.append(i)
            else:
                bolinmaydi.append(i)
        return sum(bolinmaydi) - sum(bolinadi)

