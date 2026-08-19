class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for x in range(len(prices)):
            for y in range(x+1,len(prices)):
                result = max(result,prices[y]-prices[x])

        return result