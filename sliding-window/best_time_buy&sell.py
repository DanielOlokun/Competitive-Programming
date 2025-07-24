You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        sell = 1

        max_profit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)   # ***NB***
            else:
                buy = sell        # but becomes sell as sell is constantly moving as seen in next line -- > therefore based on the if statement if sell is less than buy, the if statement is not true and but MUST become sell
            sell += 1

        return max_profit
