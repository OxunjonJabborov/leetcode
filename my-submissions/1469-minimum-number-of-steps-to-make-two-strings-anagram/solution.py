class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        steps = 0
        for diff in count:
            if diff > 0:
                steps += diff
        return steps
