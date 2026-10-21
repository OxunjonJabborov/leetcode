class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        for i in range(len(names)):
            for j in range(len(names) - i - 1):
                if heights[j] < heights[j + 1]:
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    names[j], names[j + 1] = names[j + 1], names[j]
        return names