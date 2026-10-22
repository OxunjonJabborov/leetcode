class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        javob = ""
        if len(strs) == 0:
            return javob
        kalit = min(strs, key=len)
        for indeks in range(len(kalit)):
            for list_elementi in strs:
                if kalit[indeks] != list_elementi[indeks]:
                    return javob
            javob += kalit[indeks]
        return javob
