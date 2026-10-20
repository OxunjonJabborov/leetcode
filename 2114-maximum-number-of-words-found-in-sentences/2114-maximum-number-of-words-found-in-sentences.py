class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = []
        for i in sentences:
            ans.append(i.count(" ") + 1)
        return max(ans)
