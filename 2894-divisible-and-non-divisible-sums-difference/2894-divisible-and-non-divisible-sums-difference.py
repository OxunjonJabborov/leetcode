class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        bolinadi = 0
        bolinmaydi = 0
        while n != 0:
            if n % m == 0:
                bolinadi += n
            else:
                bolinmaydi += n
            n -= 1
        return bolinmaydi - bolinadi