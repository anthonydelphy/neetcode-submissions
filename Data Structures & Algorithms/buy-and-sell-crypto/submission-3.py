class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for x in range(len(prices)):
            for y in range(x,len(prices)):
                
                print(prices[x],prices[y], prices[y]-prices[x])
                if prices[y]-prices[x] > result:
                    result = prices[y]-prices[x]

        return result