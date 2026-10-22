class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        natija = []
        for i in range(n - 2):
            qator = []
            for j in range(n - 2):
                max_qiymat = 0
                for k in range(3):
                    for l in range(3):
                        max_qiymat = max(max_qiymat, grid[i + k][j + l])
                qator.append(max_qiymat)
            natija.append(qator)
        return natija