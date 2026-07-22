class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAr = 0
        result = -1
        for i in range(len(heights)):
            for x in range(i, len(heights)):
                minHeight = min(heights[i],heights[x])
                area = (x-i) * minHeight
                if maxAr < (area):
                    maxAr = area
        return maxAr
