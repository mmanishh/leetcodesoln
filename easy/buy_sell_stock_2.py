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
        
        while i < (len(prices)-1):
            
            while (i<(len(prices)-1) and prices[i] >= prices[i+1]):
                
                i += 1
                print("valley",i)
            valley = prices[i]
            
            while (i<(len(prices)-1) and prices[i] <= prices[i+1]):
                
                i += 1
            
            peak = prices[i]
            

            print("valley andpeak",valley,peak)
            
            max_profit += peak - valley
            
        
        return max_profit


if __name__ == "__main__":

    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))    