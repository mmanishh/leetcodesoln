import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = sys.maxsize
        max_profit =  0

        for price in prices:

            if price<min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price


        return max_profit


if __name__ == "__main__":

    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))    