class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_profit = float('inf')
        max_profit = 0
        for i in prices:
            if i<min_profit:
                min_profit = i
            if  i - min_profit > max_profit:
                max_profit = i - min_profit
        return max_profit            
