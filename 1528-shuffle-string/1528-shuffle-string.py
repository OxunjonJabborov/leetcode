class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ''
        dictionary = {}
        for i in range(len(s)):
            dictionary[indices[i]] = s[i]
        for i in range(len(s)):
            ans += dictionary[i]
        return ans