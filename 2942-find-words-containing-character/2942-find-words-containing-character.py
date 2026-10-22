class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        m = 0
        for i in words:
            if x in i:
                ans.append(m)
            m+=1
        return ans