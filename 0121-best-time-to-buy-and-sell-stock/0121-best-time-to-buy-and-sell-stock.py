class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock_value = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < stock_value:
                stock_value = prices[i]

            else: 
                profit = max(profit, prices[i] - stock_value) 

        return profit