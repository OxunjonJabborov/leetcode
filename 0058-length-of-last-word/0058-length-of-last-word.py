class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        soni = 0
        s = s.rstrip()
        if len(s) == 1:
            return 1
        for i in range(1, len(s) + 1):
            if s[-i] == ' ':
                break
            else:
                soni += 1
        return soni