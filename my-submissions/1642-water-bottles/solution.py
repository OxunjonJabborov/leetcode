class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        javob = numBottles
        
        while numBottles >= numExchange:
            javob += numBottles // numExchange
            numBottles = (numBottles // numExchange) + (numBottles % numExchange)
        return javob
