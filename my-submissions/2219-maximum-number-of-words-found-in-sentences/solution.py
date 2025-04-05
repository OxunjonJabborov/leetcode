class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        k = 0
        for i in sentences:
            sozlar_soni = i.count(" ") + 1
            k = max(sozlar_soni, k)
        return k
