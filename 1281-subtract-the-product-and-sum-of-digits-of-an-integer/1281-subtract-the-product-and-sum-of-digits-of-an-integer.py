class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        kop = 1
        yig = 0
        for i in s:
            kop *= int(i)
            yig += int(i)
        return kop - yig