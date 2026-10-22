class Solution:
    def isPalindrome(self, x: int) -> bool:
       if x < 0: return False
       s = str(x)
    #    s2 = s[::-1]
       if s == s[::-1]: return True
       else: return False
       