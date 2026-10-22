class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_polindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                skip_left = is_polindrome(left + 1, right)
                skip_right = is_polindrome(left, right - 1)
                return skip_left or skip_right
                return True
            left += 1
            right -= 1
        return True