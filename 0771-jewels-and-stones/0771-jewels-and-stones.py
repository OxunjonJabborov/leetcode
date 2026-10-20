class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 1-usul. Junior paytimdagi :)
        # k = 0
        # for i in stones:
        #     if i in jewels:
        #         k += 1
        # return k
        # 2-usul. Middle paytimdagi :)
        jewels_set = set(jewels)
        return sum(stone in jewels_set for stone in stones)