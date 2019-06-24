import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        i = 0
        valley = prices[0]
        peak = prices[0]
        max_profit = 0
        
        for i in range(1,len(prices)-1):

            if prices[i+1] > prices[i]:
                max_profit += prices[i+1]-prices[i]
        return max_profit

if __name__ == "__main__":

    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))    