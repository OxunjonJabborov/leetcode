class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        k = max(candies)
        for i in candies:
            ans.append(k <= i + extraCandies)
        return ans