class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        # 731 ms Too bad
        # for i in range(len(names)):
        #     for j in range(len(names) - i - 1):
        #         if heights[j] < heights[j + 1]:
        #             heights[j], heights[j + 1] = heights[j + 1], heights[j]
        #             names[j], names[j + 1] = names[j + 1], names[j]
        # return names

        heights_to_dict = dict(zip(heights, names))
        return [heights_to_dict[n] for n in sorted(heights, reverse=True)]