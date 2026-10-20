class Solution:
    def maxFreqSum(self, s: str) -> int:
        undosh = []
        unli = []
        s1 = set(s)
        for i in s1:
            if i in ['a', 'e', 'i', 'o', 'u']:
                unli.append(s.count(i))
            else:
                undosh.append(s.count(i))
        max_unli = max(unli) if unli else 0
        max_undosh = max(undosh) if undosh else 0
        return max_unli + max_undosh