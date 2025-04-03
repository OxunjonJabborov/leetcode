class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        m = 0
        n = 0
        for i in operations:
            if "+" in i:
                m += 1
            elif "-" in i:
                n -= 1
        return m + n
