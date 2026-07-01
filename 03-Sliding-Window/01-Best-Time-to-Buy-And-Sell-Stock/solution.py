from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit from buying and selling a stock once.
        
        :param prices: List of daily stock prices.
        :return: Maximum possible profit. Returns 0 if no profit can be made.
        """
        if not prices:
            return 0
            
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            # Update the minimum price encountered so far
            if price < min_price:
                min_price = price
            # Check if selling at the current price yields a better profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit