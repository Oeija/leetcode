class Solution(object):
    def maxProfit(self, prices):

        n = len(prices)
        margin = [0] * n

        for x in range(n):
            if x != n-1:
                margin[x] = prices[x+1] - prices[x]
        
        m = len(margin)
        result = 0

        for x in range(m):
            if margin[x] > 0:
                result += margin[x]

        return result
        