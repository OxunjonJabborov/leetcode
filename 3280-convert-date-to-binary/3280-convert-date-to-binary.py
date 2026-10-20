class Solution:
    def convertDateToBinary(self, date: str) -> str:
        yil, oy, kun = date.split('-')
        def ikkilikka_ot(n: int) -> str:
            ikkilik = ""
            while n > 0:
                ikkilik = str(n % 2) + ikkilik
                n = n // 2
            return ikkilik
        yil = ikkilikka_ot(int(yil))
        oy = ikkilikka_ot(int(oy))
        kun = ikkilikka_ot(int(kun))
        return f'{yil}-{oy}-{kun}'