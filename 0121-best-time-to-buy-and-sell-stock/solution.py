class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        foyda, min_narx = 0, prices[0]
        
        for narx in prices:
            if min_narx > narx:
                min_narx = narx
            elif narx - min_narx > foyda:
                foyda = narx - min_narx

        return foyda
