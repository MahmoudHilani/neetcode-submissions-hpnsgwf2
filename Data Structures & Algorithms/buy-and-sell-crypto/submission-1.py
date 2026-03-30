class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        profit = 0
        for r,x in enumerate(prices):
            if x < prices[l]:
                l = r
            if x - prices[l] > profit:
                profit = x - prices[l]
                
        return profit
            