class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        k = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] == words[j][::-1]:
                    k += 1
        return k

